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



ans_count_file='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/ESEM/FullData_PuppetMarch21.csv'
ans_count_dict=getAnswerCount(ans_count_file)
# print ans_count_dict
