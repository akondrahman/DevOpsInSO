# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:37:47 2016

@author: akond
"""



from lxml import etree
import sys, utility
from multiprocessing import Pool
from contextlib import closing
import multiprocessing

reload(sys)
sys.setdefaultencoding('utf-8')
TAG = 'row'

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

def process_element(elem, fout, id_):
        creation_date_str, socre_str, owner_uid_str, last_edit_uid_str = "", "", "", "" 
        last_edit_date_str, last_act_date_str, cnt_str = "", "", ""
        # get post
        postID = elem.attrib['Id']
        if (len(postID) > 0 ):
          postID = int(postID)
        else: 
          postID=0  
        if postID==id_: 
          # get creation date
          if 'CreationDate' in elem.attrib:
            creation_date_str   = elem.attrib['CreationDate']
          else:
            creation_date_str   = 'NA'               
          # get score 
          if 'Score' in elem.attrib:
            socre_str   = elem.attrib['Score']
          else:
            socre_str   = str(0)   
                        
          # get owner user id
          if 'OwnerUserId' in elem.attrib:
            owner_uid_str   = elem.attrib['OwnerUserId']
          else:
            owner_uid_str   = str(0)             

          # get last editor user id
          if 'LastEditorUserId' in elem.attrib:
            last_edit_uid_str   = elem.attrib['LastEditorUserId']
          else:
            last_edit_uid_str   = str(0)

            
          # get LastEditDate
          if 'LastEditDate' in elem.attrib:
            last_edit_date_str   = elem.attrib['LastEditDate']
          else:
            last_edit_date_str   = 'NA'  

          # get LastActivityDate
          if 'LastActivityDate' in elem.attrib:
            last_act_date_str   = elem.attrib['LastActivityDate']
          else:
            last_act_date_str   = 'NA' 

          # get CommentCount
          if 'CommentCount' in elem.attrib:
            cnt_str   = elem.attrib['CommentCount']
          else:
            cnt_str   = str(0)   
          str1 = str(postID) + "," + creation_date_str + "," + socre_str + "," + owner_uid_str + ","             
          str2 = last_edit_uid_str+ "," + last_edit_date_str + "," + last_act_date_str + "," + cnt_str 
          strToDump = str1 + str2 + " "        
          print >>fout, strToDump.replace('\n', ' ')
          strToDump=""  
          
          
          


def main(idList):
    fileToRead = dirName + '/' + 'Posts.xml'
    outputFile =   dirName + '/' + '.anser_details.csv'
    fin =  open(fileToRead, 'r')
    fout = open(outputFile, 'w')


    context = etree.iterparse(fin)
    fast_iter(context, process_element, fout, idList)



if __name__ == "__main__":
    print "Started at:", utility.giveTimeStamp()
    multi_processed_output=[]
    strTooutput=''
    dirName_='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/question_ids/'
    inputSrc_ = 'so_.csv'
    print "The file is called:", inputSrc_
    file2read =  dirName_ + inputSrc_

    allTheIds= utility.readCSVForKeywords(file2read)
    print "Number of answers to find out:", len(allTheIds) 
    ### multi processing zone
    no_of_threads = 2
    #no_of_threads = multiprocessing.cpu_count()
    print "Count of threads that will be used:", no_of_threads
    with closing(Pool(processes=no_of_threads)) as pool:
      with utility.duration():
        ids2Search = allTheIds[0]  
        multi_processed_output = pool.map(main, ids2Search)
        pool.terminate()


    print "Ended at:", utility.giveTimeStamp()        