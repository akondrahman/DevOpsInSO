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




def loadDatasetByUnsatisfaction(path_to_file):
  rq2Dict={}
  with open(path_to_file, 'rU') as f:
     reader_ = csv.reader(f)
     next(reader_)
     for row_ in reader_:
       satisfactionStatus  = row_[1]
       challenge           = row_[5]
       if (len(satisfactionStatus)==0):
          if challenge not in rq2Dict:
             rq2Dict[challenge] = [satisfactionStatus]
          else:
             rq2Dict[challenge] =  rq2Dict[challenge] + [satisfactionStatus]
  return rq2Dict

def loadDatasetByChallenge(path_to_file):
  qDict={}
  with open(path_to_file, 'rU') as f:
     reader_ = csv.reader(f)
     next(reader_)
     for row_ in reader_:
       qID              = row_[0]
       challenge        = row_[5]
       if challenge not in qDict:
           qDict[challenge] = [qID]
       else:
           qDict[challenge] =  qDict[challenge] + [qID]
  return qDict


def provideAnswerToRQ2(sat_, unsat_, q_, count):
    for challenge_, sat_elems_list in sat_.items():
        sat_count   = len(sat_elems_list)
        unsat_count = len(unsat_[challenge_])
        ques_count  = len(q_[challenge_])
        #print "Q:{}, S:{}, U:{}".format(ques_count, sat_count, unsat_count)
        sat_perc    = round(float(sat_count)/float(ques_count), 5)*100
        unsat_perc  = round(float(unsat_count)/float(ques_count), 5)*100
        print "Challenge:{}, Q-Count:{}, Sat(%):{}, Unsat(%):{}".format(challenge_, ques_count, sat_perc, unsat_perc)
        print "*"*50


# datasetFile='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/ESEM/COMPLETE_DATASET_FOR_PAPER.csv'
datasetFile='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/ESEM/Upto2016/COMPLETE_DATASET_FOR_PAPER.csv'
rq2SatDict, countOfQs = loadDatasetBySatisfaction(datasetFile)
print "We will be analyzing {} questions".format(countOfQs)
print "="*100
rq2UnsatDict = loadDatasetByUnsatisfaction(datasetFile)
print "Loaded unsatosfactory dict"
print "="*100
rq2QCountDict = loadDatasetByChallenge(datasetFile)
print "Loaded question count dict"
print "="*100
provideAnswerToRQ2(rq2SatDict, rq2UnsatDict, rq2QCountDict, countOfQs)
print "="*100
