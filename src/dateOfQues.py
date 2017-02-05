'''
Akond Rahman: Dec 01, 2016
'''
import os, csv, xlrd, collections

def extractMonthWiseQCount(fileP):
  dateAndQHolder={}
  with open(fileP, 'rU') as f1:
    reader1 = csv.reader(f1)
    next(reader1, None)
    for row_ in reader1:
      dateOfQues = row_[1]
      #print dateOfQues
      IDOfQues   = row_[3]
      if ('/' in dateOfQues):
        splittedDate = dateOfQues.split('/')
        monthOfQues  = splittedDate[0]
        if (len(monthOfQues)==1):
          monthOfQues = "0" + monthOfQues
        yearOfQues   = splittedDate[2]
        date2Use     = "20" + yearOfQues + '-' + monthOfQues
      elif ('-' in dateOfQues):
        splittedDate = dateOfQues.split('-')
        yearOfQues   = splittedDate[0]
        monthOfQues  = splittedDate[1]
        date2Use     = yearOfQues + "-" + monthOfQues
      #print date2Use
      if date2Use not in dateAndQHolder:
        dateAndQHolder[date2Use] = [ IDOfQues ]
      else:
        dateAndQHolder[date2Use] = dateAndQHolder[date2Use] + [ IDOfQues ]
  print "dates:", len(dateAndQHolder)


file2read="/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq1/you_are_never_done/_TrendInp.csv"
extractMonthWiseQCount(file2read)
