'''
RQ3: ESEM
Akond Rahman
March 25, 2017
'''
import csv, os, numpy as np, utility



def loadDatasetByView(path_to_file):
  rq3Dict={}
  totalLineCount = 0
  with open(path_to_file, 'rU') as f:
     reader_ = csv.reader(f)
     next(reader_)
     for row_ in reader_:
       totalLineCount = totalLineCount + 1
       viewCount        = row_[3]
       challenge        = row_[5]
       if challenge not in rq3Dict:
           rq3Dict[challenge] = [viewCount]
       else:
           rq3Dict[challenge] =  rq3Dict[challenge] + [viewCount]
  return rq3Dict, totalLineCount





datasetFile='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/ESEM/COMPLETE_DATASET_FOR_PAPER.csv'
rq3Dict, countOfQs = loadDatasetByView(datasetFile)
print "We will be analyzing {} questions".format(countOfQs)
print "="*100
