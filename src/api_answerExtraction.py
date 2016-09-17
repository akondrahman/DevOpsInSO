# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:15:59 2016

@author: akond
"""



import  utility, stackexchange, time , os 
#from stackauth import StackAuth



def _insertDataInDB(tableParam, ans_details):
  import db_connection
  connection = db_connection.giveConnection()        
  try:

    with connection.cursor() as cursor:
      tableFieldStr1 = "AnsId,  CreationDate, LastActivityDate, Score" 
      tableFieldStr = "`" + tableParam  + "`(" +  tableFieldStr1   + ")"
      inseSttmt = "INSERT INTO " + tableFieldStr + " VALUES (%s, %s, %s, %s)"
      dataToInserTuple = (ans_details[0], ans_details[1], ans_details[2], ans_details[3])
      cursor.execute(inseSttmt,  dataToInserTuple)
      connection.commit()
  finally:
    connection.close()  


def extractAnswerDetailsViaAPI(ansList, so_obj, tableNameP):
  cnt_ =0
  idList = [int(x_) for x_ in ansList ]
  ansDetailsList = so_obj.answers(idList)
  allTples=[]
  print "Response from API contains {} elemnts".format(len(ansDetailsList))
  for ans_ in ansDetailsList:
    print "The record is:", ans_
    cnt_ = cnt_ + 1 
    id_ = ans_.id  
    create_date = ans_.creation_date.strftime('%Y-%m-%d %H:%M:%S')  
    last_act_date = ans_.last_activity_date.strftime('%Y-%m-%d %H:%M:%S')
    #owner_id = ans_.owner_id
    score_ = ans_.score
    
    #rep_ = getOwnerRep(so_obj, owner_id)
    tupToInsert = (str(id_), create_date, last_act_date,  str(score_))
    #_insertDataInDB(tableNameP, tupToInsert)
    allTples.append(tupToInsert)
    print "So far {} records processed ...".format(cnt_)    
  return allTples


def giveProcessedStr(listParam):
  str_=""
  for tup_ in listParam:
    tmp_= ""  
    for elem in tup_:
      tmp_ =tmp_ + elem + ","
    str_ = str_ + tmp_ + "\n"
  return str_  
if __name__ == "__main__":
    allContent =[]
    print "Started at:", utility.giveTimeStamp()
    dirName_='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/question_ids/stack_overflow_2/'
    tableName='dummy'
    so_obj = stackexchange.StackOverflow()
    for root, dirs, files in os.walk(dirName_):
       for file_ in files:   
        if file_.endswith(".csv"):
             print "Skipping ..."
        else:     
            print "The file is called:", file_
            file2read =  dirName_ + file_
            allTheIds= utility.readCSVForKeywords(file2read)
            print "Number of answers to find out:", len(allTheIds) 
            tuples_  = extractAnswerDetailsViaAPI(allTheIds, so_obj, tableName)
            allContent = allContent + tuples_ #tuples_ is a list of tuples 

        time.sleep(150)
    strToDump = giveProcessedStr(allContent)    
    status_ = utility.dumpContentIntoFile(strToDump, "ans_stack_overflow_2_all.csv")
    print "Dumped a file of {} bytes".format(status_)