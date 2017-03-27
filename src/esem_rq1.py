'''
RQ1: ESEM
Akond Rahman
March 25, 2017
'''
import csv, os, numpy as np, utility



def loadDatasetByChallenge(path_to_file):
  rq1Dict={}
  totalLineCount = 0
  with open(path_to_file, 'rU') as f:
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





def provideAnswerToRQ1(dict_, count_):
    for challenge_, qs in dict_.items():
        perc_ = round((len(qs))/(float(count_)), 4)
        perc_ = perc_ * 100
        print "Challenge:{}, percenatge:{}".format(challenge_, perc_)
        print "*"*50


# datasetFile='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/ESEM/COMPLETE_DATASET_FOR_PAPER.csv'
datasetFile='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/ESEM/Upto2016/COMPLETE_DATASET_FOR_PAPER.csv'
rq1Dict, countOfQs = loadDatasetByChallenge(datasetFile)
print "We will be analyzing {} questions".format(countOfQs)
print "="*100
provideAnswerToRQ1(rq1Dict, countOfQs)
