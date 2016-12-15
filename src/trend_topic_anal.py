'''
Akond, trends of topics
'''

import csv

def formatQues(dateStr):
   dstr=''
   splitted_  = dateStr.split('/')
   tmp_month_     = splitted_[0]
   tmp_year_      = splitted_[-1]
   if len(tmp_year_) == 2:
      year_ = '20' + tmp_year_
   elif len(tmp_year_) >= 4:
      year_splitted = tmp_year_.split('-')
      year_  = year_splitted[0]
   if len(tmp_month_) >= 4:
      month_splitted = tmp_month_.split('-')
      month_  = month_splitted[1]
   else:
      month_  = tmp_month_
   if len(month_)==1:
     month_ = '0' + month_
   dstr       = year_ + '-' + month_
   print dstr
   return dstr

def getDateWiseDict(fileNameParam):
  dateWiseDict={}
  with open(fileNameParam, 'rU') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
      idOfQues      = int(row[0])
      date_         = row[1]
      topicIDOfQues = int(row[2])
      origIDOfQues  = int(row[3])
      dateOfQues    = formatQues(date_)
      tupToInsert=(idOfQues, topicIDOfQues)
      if dateOfQues not in dateWiseDict:
        dateWiseDict[dateOfQues]= [tupToInsert]
      else:
        tmp_ = dateWiseDict[dateOfQues]
        dateWiseDict[dateOfQues]  = tmp_ + [tupToInsert]
  return dateWiseDict


f_ = '/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq2/RQ2_QAA_TrendInp.csv'
dateDict=getDateWiseDict(f_)
#print dateDict