'''
RQ1: ESEM
Akond Rahman
March 25, 2017
'''
import csv, os, numpy as np, utility



def loadDatasetByChallenge(path_to_file):
  rq1Dict={}
  totalLineCount = 0
  with open(file_, 'rU') as f:
     reader_ = csv.reader(f)
     next(reader_)
     for row_ in reader_:
       totalLineCount = totalLineCount + 1
       qID              = row_[0]
       challenge        = row_[5]
       if challenge not in rq1Dict:
           rq1Dict[challenge] = [qID]
       else:
           rq1Dict[challenge] =  rq1Dict[challenge] + [qID]            
  return rq1Dict, totalLineCount
