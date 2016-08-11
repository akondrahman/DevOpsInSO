from lxml import etree
import sys, utility
from multiprocessing import Pool
from contextlib import closing
import multiprocessing

reload(sys)
sys.setdefaultencoding('utf-8')
TAG = 'row'
matchedCount = 0
dirName='stackoverflow.com-Posts'

# excerpted from http://baraujo.net/blog/?p=81
# this link also helped: https://docs.python.org/2/library/xml.etree.elementtree.html

def get_unicode(strOrUnicode, encoding='utf-8'):
    if isinstance(strOrUnicode, unicode):
        return strOrUnicode
    return unicode(strOrUnicode, encoding, errors='ignore')

def fast_iter(context, func, *args, **kwargs):
    # http://www.ibm.com/developerworks/xml/library/x-hiperfparse/
    # Author: Liza Daly
    # modified to call func() only in the event and elem needed
    for event, elem in context:
        if event == 'end' and elem.tag == TAG:
            func(elem, *args, **kwargs)
        elem.clear()
        while elem.getprevious() is not None:
            del elem.getparent()[0]
    del context

def process_element(elem, fout, tagElementParam):
        global bodyAndTagMatchCount, matchedCount
        # get body
        if 'Body' in elem.attrib:
          body_unicoded_str  = get_unicode(elem.attrib['Body'], 'ascii')
        else:
          body_unicoded_str   = ''
        # get tags
        if 'Tags' in elem.attrib:
          tag_unicoded_str   = get_unicode(elem.attrib['Tags'], 'ascii')
        else:
          tag_unicoded_str   = 'NA'

        # get title
        if 'Title' in elem.attrib:
          title_unicoded_str   = get_unicode(elem.attrib['Title'], 'ascii')
        else:
          title_unicoded_str   = ''
        # get post
        postID = elem.attrib['Id']

        if (utility.findStringInTag( tagElementParam, tag_unicoded_str)):
          #print "Found sth. at post ID=", postID
          matchedCount = matchedCount +  1
          #print >>fout, tag_unicoded_str.replace('\n', ' ')
          if (utility.findStringInPost(body_unicoded_str)) or (utility.findStringInPost(title_unicoded_str)):
           bodyAndTagMatchCount = bodyAndTagMatchCount +  1
        #else:
          #print "Output->ID:{}, tag-element:{}, Tag-string:{}".format( postID, tagElementParam ,tag_unicoded_str )
          #print >>fout_no_param, postID.replace('\n', ' ')
        #counter += 1
        #print "So far {} lines processed".format(counter)

def main(tagElement):
    fileToRead = dirName + '/' + 'Posts.xml'
    outputFile =   dirName +  '.matching_posts_as_tags.txt'
    fin =  open(fileToRead, 'r')
    fout = open(outputFile, 'w')

    # for the non-matching IDs
    #fout_non_matching = open(non_matched_fileToOutput, 'w')
    context = etree.iterparse(fin)
    global bodyAndTagMatchCount, matchedCount
    bodyAndTagMatchCount, matchedCount = 0, 0
    fast_iter(context, process_element, fout, tagElement)
    #print "Tag: {}, matched count: {}".format(tagElement, matchedCount)
    return  tagElement, matchedCount, bodyAndTagMatchCount


if __name__ == "__main__":
    print "Started at:", utility.giveTimeStamp()
    multi_processed_output=[]
    strTooutput=''
    dirNameForBatches='batches/mac/'
    inputBatch = 'batch_eu'
    print "The file is called:", inputBatch
    matched_tags_file =  dirNameForBatches + inputBatch
    outputFile =  matched_tags_file + '_tag-stat.csv'
    allTheTags= utility.getTagsFromFormattedFile(matched_tags_file)
    tagProcCount = 1
    #for tagElem in allTheTags:
    ### multi processing zone
    #no_of_threads = len(allTheTags)
    no_of_threads = multiprocessing.cpu_count()
    print "Count of threads that will be used:", no_of_threads
    with closing(Pool(processes=no_of_threads)) as pool:
      with utility.duration():
        multi_processed_output = pool.map(main, allTheTags)
        print "Parallel output: \n", multi_processed_output
        pool.terminate()
    for outputElem in multi_processed_output:
       #outputElem[0] name of the tag
       #outputElem[1] for number of posts that match the tag
       #outputElem[2] for number of posts that match the tag and has at least one of the keywords
       strTooutput = strTooutput + outputElem[0] + ',' + str(outputElem[1]) + ',' + str(outputElem[2]) + '\n'
    dump_stat = utility.dumpContentIntoFile(strTooutput, outputFile)
    print "Dumped a file with {} bytes".format(dump_stat)
    print "Ended at:", utility.giveTimeStamp()
