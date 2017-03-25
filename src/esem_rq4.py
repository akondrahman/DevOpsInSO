'''
Akond Rahman
ESEM:RQ4
March 25, 2017
'''




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
       qID              = row_[0]
       challenge        = row_[5]
       if challenge not in rq4Dict:
           rq4Dict[challenge] = [qID]
       else:
           rq4Dict[challenge] =  rq4Dict[challenge] + [qID]
  return rq4Dict, totalLineCount





datasetFile='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/ESEM/COMPLETE_DATASET_FOR_PAPER.csv'
ques_challenge_dict = loadDatasetByChallenge(datasetFile)
print "="*100
