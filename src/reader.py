from lxml import etree
import sys, utility

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

def process_element(elem, fout):
        global counter, matchedCount

        # get body
        body_unicoded_str  = get_unicode(elem.attrib['Body'], 'ascii')
        # get title
        if 'Title' in elem.attrib:
          title_unicoded_str   = get_unicode(elem.attrib['Title'], 'ascii')
        else:
          title_unicoded_str   = ''
        # get tags
        if 'Tags' in elem.attrib:
          tag_unicoded_str   = get_unicode(elem.attrib['Tags'], 'ascii')
        else:
          tag_unicoded_str   = 'NA'
        # get posts
        postID = elem.attrib['Id']
        #print "Output->ID:{}, Body:{}".format( postID, body_unicoded_str )
        if (utility.findStringInPost(body_unicoded_str)) or (utility.findStringInPost(title_unicoded_str)):
          #print "Found sth. at post ID=", postID
          matchedCount = matchedCount +  1
          #print "Tags:content->", tag_unicoded_str
          #print "So far {} posts matched ".format(matchedCount)
          print >>fout, tag_unicoded_str.replace('\n', ' ')
        #else:
          #print >>fout_no_param, postID.replace('\n', ' ')
        counter += 1
        #print "So far {} lines processed".format(counter)

def main():

    fileToRead = dirName + '/' + 'Posts.xml'
    matched_fileToOutput =   dirName +  '.matching_tags.txt'
    #non_matched_fileToOutput = dirName + '.non_matching_ids.txt'
    fin =  open(fileToRead, 'r')
    # for the matching IDs
    fout = open(matched_fileToOutput, 'w')
    # for the non-matching IDs
    #fout_non_matching = open(non_matched_fileToOutput, 'w')
    context = etree.iterparse(fin)
    global counter, matchedCount
    counter, matchedCount = 0, 0
    fast_iter(context, process_element, fout)
    print "Total {} matching posts found!".format(matchedCount)
    print "Total {} posts analyzed".format(counter)

if __name__ == "__main__":
    with utility.duration():
         main()
