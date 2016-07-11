from lxml import etree
import sys, utility

reload(sys)
sys.setdefaultencoding('utf-8')
TAG = 'row'
matchedCount = 0

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
        #t.text = elem.find('Body').text

        body_unicoded_str  = get_unicode(elem.attrib['Body'], 'ascii')
        postID = elem.attrib['Id']
        #print "Output->ID:{}, Body:{}".format( postID, body_unicoded_str )
        if (utility.findStringInBody(body_unicoded_str)):
          print "Found sth. at post ID=", postID
          matchedCount = matchedCount +  1
          print "So far {} posts matched ".format(matchedCount)
          print >>fout, postID.replace('\n', ' ')
        counter += 1
        #print "So far {} lines processed".format(counter)

def main():
    fileToRead = 'retrocomputing.stackexchange.com/Posts.xml'
    fileToOutput = 'idHolder.txt'
    fin =  open(fileToRead, 'r')
    fout = open(fileToOutput, 'w')
    context = etree.iterparse(fin)
    global counter, matchedCount
    counter, matchedCount = 0, 0
    fast_iter(context, process_element, fout)

if __name__ == "__main__":
    with utility.duration():
         main()
