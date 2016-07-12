from lxml import etree
import sys, utility

reload(sys)
sys.setdefaultencoding('utf-8')
TAG = 'row'
matchedCount = 0
dirName='retrocomputing.stackexchange.com'

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
    return  matchedCount, bodyAndTagMatchCount


if __name__ == "__main__":
    dictToStore={}
    strTooutput=''
    matched_tags_file =   dirName +  '.matching_tags.txt'
    allTheTags= utility.getTags(matched_tags_file)
    for tagElem in allTheTags:
      with utility.duration():
         matchedPostsCnt =  main(tagElem)
         dictToStore[tagElem] = matchedPostsCnt
    for k_, v_ in dictToStore.items():
       #print "Tag->{}, Count->{}".format(k_, v_)
       #v_[0] for number of posts that match the tag
       #v_[1] for number of posts that match the tag and has at least one of the keywords  
       strTooutput = strTooutput + k_ + ',' + str(v_[0]) + ',' + str(v_[1]) + '\n'
    dump_stat = utility.dumpContentIntoFile(strTooutput, 'tag-stat.csv')
    print "Dumped a file with {} bytes".format(dump_stat)
