'''
ESEM RQ5 Preparation
Akond Rahman
March 25, 2017
'''
from collections import Counter, OrderedDict
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




def getDatesOfChallenges(datasetFile):
  rq5Dict={}
  with open(datasetFile, 'rU') as f:
     reader_ = csv.reader(f)
     next(reader_)
     for row_ in reader_:
       date_month        = row_[2]
       challenge         = row_[5]
       if challenge not in rq5Dict:
           rq5Dict[challenge] = [date_month]
       else:
           rq5Dict[challenge] =  rq5Dict[challenge] + [date_month]
  return rq5Dict


def getChallengeWiseTemporalValues(dateDict, challengeDict):
    temporalDict={}
    sortedDateKeysAsList = sorted(dateDict)
    for challenge_, date_list in challengeDict.items():
        temporal_list = []
        for month in sortedDateKeysAsList:
            cnt_per_month = dateDict[month]  ### get the count of all Puppet questions per month
            tmp_dict = dict(Counter(date_list)) ### get the count of question count for challenges
            if month in tmp_dict:
                ques_per_month = int(tmp_dict[month])
            else:
                ques_per_month = 0
            #print "month:{}, ques-per-month:{}, all-cnt-per-month:{}".format(month, ques_per_month, cnt_per_month)
            temporal_metric = round(float(ques_per_month)/float(cnt_per_month), 5)
            temporal_list.append(temporal_metric)
            temporal_metric = float(0)
        temporalDict[challenge_] =  temporal_list
    return temporalDict

datasetFile='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/ESEM/COMPLETE_DATASET_FOR_PAPER.csv'
rq5Dict = loadDatasetByDate(datasetFile)
print "We have data of {} months ... ".format(len(rq5Dict))
print "="*100
challenge_date_dict = getDatesOfChallenges(datasetFile)
print "We are looking at {} challenges ...".format(len(challenge_date_dict))
print "="*100
per_month_challenge_dict = getChallengeWiseTemporalValues(rq5Dict, challenge_date_dict)
#print per_month_challenge_dict
for k_, v_ in per_month_challenge_dict.items():
    print "challenge:{}, temporal_trend values:{}".format(k_, len(v_))
print "="*100
