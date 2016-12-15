'''
Akond, trends of topics
'''

import csv

def formatQues(dateStr):
   dstr=''
   splitted_  = dateStr.split('/')
   month_     = splitted_[0]
   year_      = splitted_[-1]
   dstr       = year_ + '-' + month_
   return dstr       

def getDateWiseDict(fileNameParam):
  dateWiseDict={}
  with open(fileNameParam, 'rU') as f:
    reader = csv.reader(f)
    next()
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



f_ = '/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq2/RQ2_QAA_TrendInp.csv'
dateDict=getDateWiseDict(f_)
print dateDict
