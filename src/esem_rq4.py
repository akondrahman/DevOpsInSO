'''
Akond Rahman
ESEM:RQ4
March 25, 2017
'''
import csv, os, numpy as np, utility



def loadDatasetByChallenge(path_to_file):
  rq1Dict={}
  with open(path_to_file, 'rU') as f:
     reader_ = csv.reader(f)
     next(reader_)
     for row_ in reader_:
       qID              = row_[0]
       challenge        = row_[5]
       if challenge not in rq1Dict:
           rq1Dict[challenge] = [qID]
       else:
           rq1Dict[challenge] =  rq1Dict[challenge] + [qID]
  return rq1Dict


def loadDatasetByProgrammerCount(path_to_file):
  rq4Dict={}
  totalLineCount = 0
  with open(path_to_file, 'rU') as f:
     reader_ = csv.reader(f)
     next(reader_)
     for row_ in reader_:
       totalLineCount = totalLineCount + 1
       programmerID     = row_[4]
       challenge        = row_[5]
       if challenge not in rq4Dict:
           rq4Dict[challenge] = [programmerID]
       else:
           rq4Dict[challenge] =  rq4Dict[challenge] + [programmerID]
  return rq4Dict, totalLineCount





def provideAnswerToRQ4(p_dict_, q_dict):
    for challenge_, qs in q_dict.items():
        q_count = len(qs)
        p_count = len(np.unique(p_dict_[challenge_]))
        print "Challenge: {}, programmer count:{}, ques count:{}".format(challenge_, p_count, q_count)
        #print "Challenge:{}, percenatge:{}".format(challenge_, perc_)
        print "*"*50



datasetFile='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/ESEM/COMPLETE_DATASET_FOR_PAPER.csv'
ques_challenge_dict = loadDatasetByChallenge(datasetFile)
print "Loaded the questions for each challenge"
print "="*100
programmer_dict, qcount =loadDatasetByProgrammerCount(datasetFile)
print "We will be analyzing {} questions".format(qcount)
print "="*100
provideAnswerToRQ4(programmer_dict, ques_challenge_dict)
print "="*100
