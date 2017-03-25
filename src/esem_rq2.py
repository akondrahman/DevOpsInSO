'''
RQ1: ESEM
Akond Rahman
March 25, 2017
'''
import csv, os, numpy as np, utility



def loadDatasetBySatisfaction(path_to_file):
  rq2Dict={}
  totalLineCount = 0
  with open(path_to_file, 'rU') as f:
     reader_ = csv.reader(f)
     next(reader_)
     for row_ in reader_:
       totalLineCount = totalLineCount + 1
       satisfactionStatus  = row_[1]
       challenge           = row_[5]
       if (len(satisfactionStatus)>0):
          if challenge not in rq2Dict:
             rq2Dict[challenge] = [satisfactionStatus]
          else:
             rq2Dict[challenge] =  rq2Dict[challenge] + [satisfactionStatus]
  return rq2Dict, totalLineCount




datasetFile='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/ESEM/COMPLETE_DATASET_FOR_PAPER.csv'
rq2SatDict, countOfQs = loadDatasetBySatisfaction(datasetFile)
print "We will be analyzing {} questions".format(countOfQs)
print "="*100
