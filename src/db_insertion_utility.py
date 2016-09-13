# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 10:26:55 2016

@author: akond
"""



def _insertDataInDB(tableParam, allListParam):
  import db_connection
  cnt = 0
  for listParam in allListParam:
    cnt = cnt + 1   
    print "# of records processed:", cnt  
    #print listParam[0]
    try:
      connection = db_connection.giveConnection()        
      with connection.cursor() as cursor:
        tableFieldStr1 = "Id,  PostTypeId, AcceptedAnswerId, ParentID, CreationDate, DeletionDate, Score, ViewCount, OwnerUserId, " 
        tableFieldStr2 = "OwnerDisplayName,  LastEditorUserId, LastEditDate, LastActivityDate, AnswerCount, CommentCount, FavoriteCount, ClosedDate"
        tableFieldStr = "`" + tableParam  + "`(" +  tableFieldStr1 + tableFieldStr2  + ")"
        inseSttmt = "INSERT INTO " + tableFieldStr + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        id_ = listParam[0]
        post_type_id_ = listParam[1]
        accepted_ans_id_   = listParam[2]         
        parent_id_ = listParam[3]
        score_ = listParam[6]
        vcount_ = listParam[7] 
        owner_user_id_ = listParam[8]
        last_editor_user_id_ = listParam[10]
        ans_count = listParam[13]
        comment_count = listParam[14]
        fav_count = listParam[15]
        closed_date = listParam[16]        
          
        
        if (len(id_) <= 0):
          id_=str(0)    
        if (len(accepted_ans_id_) <= 0):
          accepted_ans_id_=str(0)              
        if (len(post_type_id_) <= 0):
          post_type_id_=str(1000)     
        if (len(parent_id_) <= 0):
          parent_id_=str(0)               
        if (len(score_) <= 0):
          score_=str(0)                         
        if (len(vcount_) <= 0):
          vcount_=str(-9999)                         
        if (len(owner_user_id_) <= 0):
          owner_user_id_=str(0)      
        if (len(last_editor_user_id_) <= 0):
          last_editor_user_id_=str(0) 
        if (len(ans_count) <= 0):
          ans_count=str(0)                                   
        if (len(comment_count) <= 0):
          comment_count=str(0)    
        if (len(fav_count) <= 0):
          fav_count=str(0)    
        if (len(fav_count) <= 0):
          fav_count=str(0)                               
        #print ans_count
        dataToInserTuple = (
                            id_, post_type_id_, accepted_ans_id_, parent_id_, str(listParam[4]),  
                            str(listParam[5]), score_, vcount_, owner_user_id_, str(listParam[9]),
                            last_editor_user_id_, str(listParam[11]), str(listParam[12]), ans_count, comment_count, fav_count,
                            closed_date 
                           )
        cursor.execute(inseSttmt,  dataToInserTuple)
        connection.commit()
    finally:
        connection.close()  




def getDataFromCSV(fileNameParam):
  import csv
  dataList = []
  with open(fileNameParam, 'rU') as f:
    reader = csv.reader(f)
    next(reader, None)  # skip the headers    
    for row in reader:
      tmp_ = []
      for elems in row:
           tmp_.append(elems)
      #print tmp_     
      dataList.append(tmp_)           
  return dataList

dirName="/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/"
fileName="no_txt_all_so_"
csvFileName= dirName + fileName+".csv"
tupleToInsert= getDataFromCSV(csvFileName)
print "Total records retrieved: ", len(tupleToInsert)
#print tupleToInsert
_insertDataInDB(fileName, tupleToInsert )