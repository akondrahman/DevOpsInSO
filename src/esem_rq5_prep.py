'''
ESEM RQ5 Preparation
Akond Rahman
March 25, 2017
'''
from collections import Counter
import csv, os, numpy as np, utility


def loadDatasetByDate(path_to_file):
  rq5Dict={}
  dateHolder = []
  with open(path_to_file, 'rU') as f:
     reader_ = csv.reader(f)
     next(reader_)
     for row_ in reader_:
       date_month        = row_[2]
       dateHolder.append(date_month)
  rq5Dict = dict(Counter(dateHolder))
  return rq5Dict




datasetFile='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/ESEM/COMPLETE_DATASET_FOR_PAPER.csv'
rq5Dict = loadDatasetByDate(datasetFile)
print "We have data of {} months".format(rq5Dict)
print "="*100
