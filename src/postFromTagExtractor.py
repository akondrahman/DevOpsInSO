from lxml import etree
import sys, utility

reload(sys)
sys.setdefaultencoding('utf-8')
TAG = 'row'

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
        global  matchedPosts, matchedCount
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
          matchedPosts.append(postID)
          #print >>fout, tag_unicoded_str.replace('\n', ' ')


def extractPostIDsFromTag(tagElement):
    fileToRead = dirName + '/' + 'Posts.xml'
    outputFile =   dirName +  '.matching_posts_as_tags.txt'
    fin =  open(fileToRead, 'r')
    fout = open(outputFile, 'w')


    context = etree.iterparse(fin)
    global  matchedPosts, matchedCount
    matchedPosts = []
    matchedCount = 0
    fast_iter(context, process_element, fout, tagElement)
    return  matchedCount, matchedPosts


if __name__ == "__main__":
    allThePosts = []
    matched_tags_file =   dirName + '/' + 'final_tags.txt'
    allTheTags= utility.getFormattedTags(matched_tags_file)
    for tagElem in allTheTags:
      with utility.duration():
         matchedPostTup =  extractPostIDsFromTag(tagElem)
         # matchedPosts[0] gives the counter
         # matchedPosts[1] gives the matching posts
         verifyingCount = matchedPostTup[0]
         thePosts = matchedPostTup[1]
         matchedPostCount = len(thePosts)
         print"Tag:{}, count:{}, veryfying count:{}".format(tagElem, matchedPostCount, verifyingCount)
         for post in thePosts:
           allThePosts.append(post)
    print "All posts: ", len(allThePosts)
