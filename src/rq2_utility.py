# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 09:43:26 2016

@author: akond
"""



from dateutil.parser import parse
import csv, db_connection, datetime , utility
def getAnsDictFromCSV(csvParam):
  dict2Ret={}    
  with open(csvParam, 'rU') as f:
    reader = csv.reader(f)
    next(reader, None)  # skip the headers        
    for row in reader:
      id_ = int(row[0]) # id 
      create_date = row[1] # creation date of answer 
      act_date = row[2] # last activity date of answer , not so important 
      score = int(row[3]) # score of answer 
      dict2Ret[id_] = (create_date, act_date, score)
  return dict2Ret    
  
  
def getQuestionRecordFromDB(srcNameParam):
  result={}    
  tableName =  "no_txt_all_" + srcNameParam + "_"
  queryStr1 = "SELECT `AcceptedAnswerId`, `CreationDate`, `Score`, `ViewCount`, `AnswerCount`, `CommentCount`, `FavoriteCount` FROM `" + tableName + "` " 
  queryStr2 = " WHERE `AcceptedAnswerId` > 0 ;"
  sqlStr =   queryStr1 + queryStr2
  connection = db_connection.giveConnection()
  try:
    with connection.cursor() as cursor:
     cursor.execute(sqlStr)
     result = cursor.fetchall()
  finally:
    connection.close()  
  return result



def getFormattedRecordOfAnswer(srcParam):
    questionDicts = getQuestionRecordFromDB(srcParam)
    allQDicts = {}
    for dictItem in questionDicts:
      acc_ans_id = dictItem['AcceptedAnswerId'] 
      creat_date = dictItem['CreationDate']
      score_     = dictItem['Score']
      view_count = dictItem['ViewCount'] 
      ans_count  = dictItem['AnswerCount'] 
      com_count  = dictItem['CommentCount'] 
      fav_count  = dictItem['FavoriteCount']
      if acc_ans_id not in allQDicts:      
        allQDicts[acc_ans_id]  = (creat_date, score_, view_count, ans_count, com_count, fav_count)

    return allQDicts    
    
    
def createRQ2Report(ques_dict_param, andw_dict_param): 
  match_cnt = 0     
  rq2_ans_as_list = []  
  for k_, v_ in ques_dict_param.items():
    if k_ in andw_dict_param:
      match_cnt = match_cnt + 1
      # uitems related to question 
      q_create_date = v_[0] 
      q_score       = v_[1]
      q_v_cnt       = v_[2] 
      q_ans_cnt     = v_[3] 
      q_com_cnt     = v_[4]
      q_fav_cnt     = v_[5]
      
      # uitems related to answer 
      matched_answ  = andw_dict_param[k_] 
      a_create_date = matched_answ[0]  
      a_act_date    = matched_answ[1] ### will not use 
      a_score       = matched_answ[2]
      # get time difference 
      q_date_time  = parse(q_create_date)       
      a_date_time  = parse(a_create_date)   
      diff_in_minutes  = (a_date_time-q_date_time).total_seconds() / float(60)
      ### abnormal results for ask ubintu in case of time difference ... will not be used 
      #print "Q:{}, A:{}, diff:{}".format(q_date_time, a_date_time,  diff_in_minutes )
      #tup_ =(q_score, q_v_cnt, q_ans_cnt, q_com_cnt, q_fav_cnt, a_score, diff_in_minutes) 
      tup_ =(q_score, q_v_cnt, q_ans_cnt, q_com_cnt, q_fav_cnt, a_score) 
      rq2_ans_as_list.append(tup_)
  
  return rq2_ans_as_list    
def dumpFinalReport(listParam, headerParam, file2save):  
  str2write = headerParam + "\n"
  str_=""
  for tup_ in listParam:
    for elem in tup_:
      str_ = str_  + str(elem) + ","  # a commana after each elemnt in tuple 
    # a new line after each tupel   
    str_ = str_ + '\n'
  str2write = str2write + str_   
  status_ = utility.dumpContentIntoFile(str2write, file2save)
  return status_