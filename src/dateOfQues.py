'''
Akond Rahman: Dec 01, 2016
'''
import os, csv, xlrd, collections

def extractMonthWiseQCount(fileP):
  with open(fileP, 'rU') as f1:
    reader1 = csv.reader(f1)
    next(reader1, None)
    for row_ in reader1:
      dateOfQues = row_[1]
      IDOfQues   = row_[3]
      splittedDate = dateOfQues.split('/')
      monthOfQues  = splittedDate[0]
      yearOfQues   = splittedDate[2]
