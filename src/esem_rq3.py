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
def getSummationViews(dict_):
    viewHolder = []
    for challenge_, views in dict_.items():
        for view in views:
            viewHolder.append(view)
    viewHolder = [int(view_) for view_ in viewHolder ]
    return sum(viewHolder)



def provideAnswerToRQ3(dict_, view_count, ques_dict):
    for challenge_, views_ in dict_.items():
        views_               = [int(view) for view in views_]
        sum_view_count       = sum(views_)
        #print "challenge:{}, sum_view:{}".format(challenge_, sum_view_count)
        ques_per_challenge   = len(ques_dict[challenge_])
        #print "challenge:{}, question count:{}".format(challenge_, ques_per_challenge)
        view_per_total_views = round(float(sum_view_count)/float(view_count), 3)*100
        view_per_questions   = round(float(sum_view_count)/float(ques_per_challenge), 2)
        print "Challenge:{}, view-based percenatge:{}, question-based percentage:{}".format(challenge_, view_per_total_views, view_per_questions)
        print "*"*50


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

datasetFile='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/ESEM/COMPLETE_DATASET_FOR_PAPER.csv'
rq3Dict, countOfQs = loadDatasetByView(datasetFile)
print "We will be analyzing {} questions".format(countOfQs)
print "="*100
totalViewCount = getSummationViews(rq3Dict)
print "Total view count of all challenges:", totalViewCount
print "="*100
ques_dict = loadDatasetByChallenge(datasetFile)
print "="*100
provideAnswerToRQ3(rq3Dict, totalViewCount, ques_dict)
print "="*100
