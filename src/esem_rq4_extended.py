'''
Akond Rahman
ESEM:RQ4 Extended
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





def getSummationOfProgrammers(prog_dict):
    holder = []
    for k_, v_ in prog_dict.items():
       for prog_ in v_:
            holder.append(prog_)
    holder = np.unique(holder)
    return len(holder)



def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

def findIntersectingProgrammers(p_dict_):
    for challenge, progr_list in p_dict_.items():
       progr_list = np.unique(progr_list)
       print "The challenge is:{}, unique programmer count:{}".format(challenge, len(progr_list))
       rest_of_the_dict =  removekey(p_dict_, challenge)
       for rest_challenge, rest_prog_list in rest_of_the_dict.items():
           rest_prog_list = np.unique(rest_prog_list)
           common_programmers = list(set(progr_list) & set(rest_prog_list))
           denominator        = len(progr_list) + len(rest_prog_list)
           comm_prog_         = float(len(common_programmers))/float(denominator)
           comm_prog_perc     = round(comm_prog_, 5)*100
           ###print "a:{}, b:{}, a+b:{}".format(progr_list, rest_prog_list, common_programmers)
           print "--->other challenge:{}, common programmers:{}, common prog (%):{}".format(rest_challenge, len(common_programmers), comm_prog_perc)
       print "*"*50


datasetFile='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/ESEM/COMPLETE_DATASET_FOR_PAPER.csv'
ques_challenge_dict = loadDatasetByChallenge(datasetFile)
print "Loaded the questions for each challenge"
print "="*100
programmer_dict, qcount =loadDatasetByProgrammerCount(datasetFile)
print "We will be analyzing {} questions".format(qcount)
print "="*100
total_programmer_count = getSummationOfProgrammers(programmer_dict)
print "In total, {} unique programmers were involved in Puppet".format(total_programmer_count)
print "="*100
findIntersectingProgrammers(programmer_dict)
print "="*100
