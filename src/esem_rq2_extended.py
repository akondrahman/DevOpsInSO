'''
Akond RahmanMarch 27, 2017
ESEM RQ2 Extended
'''
import csv, os , numpy as np




def getAnswerCount(path_to_file):
    ansCountDict={}
    with open(path_to_file, 'rU') as f:
      reader_ = csv.reader(f)
      next(reader_)
      for row_ in reader_:
        qID              = row_[0]
        ansCount        = row_[9]
        if qID not in ansCountDict:
           ansCountDict[qID] = ansCount

    return ansCountDict



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


def provideAnswerToRQ2Extended(a_, q_):
    for challenge_, q_list in q_.items():
        ques_count  = len(q_[challenge_])
        ans_count   = 0
        for qID in q_list:
            if qID in a_:
                ans_count_of_ques = int(a_[qID])
                ans_count = ans_count + ans_count_of_ques
        print "Q:{}, A:{}".format(ques_count, ans_count)
        print "*"*50

ans_count_file='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/ESEM/FullData_PuppetMarch21.csv'
ans_count_dict=getAnswerCount(ans_count_file)
# print ans_count_dict
datasetFile='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/ESEM/Upto2016/COMPLETE_DATASET_FOR_PAPER.csv'
rq2QCountDict = loadDatasetByChallenge(datasetFile)
# print rq2QCountDict
print "Loaded question count dict"
print "="*100
provideAnswerToRQ2Extended(ans_count_dict, rq2QCountDict)
