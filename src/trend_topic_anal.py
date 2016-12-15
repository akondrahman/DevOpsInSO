'''
Akond, trends of topics
'''

import csv, collections




def formatQues(dateStr):
   dstr=''
   if ('Deletion' in dateStr) :
        dstr='2016-01'
   elif ('Creation' in dateStr):
        dstr='2016-08'        
   else:
        splitted_  = dateStr.split('/')
        tmp_month_     = splitted_[0]
        tmp_year_      = splitted_[-1]
        if len(tmp_year_) == 2:
          year_ = '20' + tmp_year_
        elif len(tmp_year_) >= 4:
          year_splitted = tmp_year_.split('-')
          year_  = year_splitted[0]
        if len(tmp_month_) >= 4:
          month_splitted = tmp_month_.split('-')
          #print month_splitted
          month_  = month_splitted[1]
        else:
          month_  = tmp_month_
        if len(month_)==1:
          month_ = '0' + month_
        dstr       = year_ + '-' + month_
   #print dstr
   return dstr

def getDateWiseDict(fileNameParam):
  dateWiseDict={}
  with open(fileNameParam, 'rU') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
      idOfQues      = row[0]
      date_         = row[1]
      topicIDOfQues = int(row[2])
      origIDOfQues  = int(row[3])
      dateOfQues    = formatQues(date_)
      tupToInsert=(idOfQues, topicIDOfQues)
      if dateOfQues not in dateWiseDict:
        dateWiseDict[dateOfQues]= [tupToInsert]
      else:
        tmp_ = dateWiseDict[dateOfQues]
        dateWiseDict[dateOfQues]  = tmp_ + [tupToInsert]
  return dateWiseDict




def getTopicWiseDict(fileNameParam):
  topicWiseDict={}
  with open(fileNameParam, 'rU') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
      date_         = row[1]
      dateOfQues    = formatQues(date_)
      topicIDOfQues = int(row[2])

      if topicIDOfQues not in topicWiseDict:
        topicWiseDict[topicIDOfQues]= [dateOfQues]
      else:
        tmp_ = topicWiseDict[topicIDOfQues]
        topicWiseDict[topicIDOfQues]  = tmp_ + [dateOfQues]
  return topicWiseDict

#f_ = '/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq1/RQ1_ALL_TrendInp.csv'
#f_ = '/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq2/RQ2_QAA_TrendInp.csv'
f_ = '/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq2/RQ2_QNAA_TrendInp.csv'
dateDict=getDateWiseDict(f_)
#print dateDict
odd = collections.OrderedDict(sorted(dateDict.items()))
#print odd
print "*"*75
trendList=[]
dateList=[]
for date_, elems in odd.iteritems():
   #print "Date:", date_
   dateList.append(date_)
   #print "Questions:", len(elems)
   trendList.append(len(elems))
   #print '*'*75
#print "For stat test:", trendList
print "All dates, sorted:", dateList
print "*"*75


topicDict = getTopicWiseDict(f_)
odt = collections.OrderedDict(sorted(topicDict.items()))
saveList=[]
for topic_, dates_ in odt.iteritems():
   print "Topic:", topic_
   dist_ques_dict     = dict(collections.Counter(dates_))
   dateWiseSortedDict = collections.OrderedDict(sorted(dist_ques_dict.items()))
   #print dist_ques
   trendPerTopicHolder = []
   for dateItem, qForTopic in dateWiseSortedDict.iteritems():
     questionsForDate = odd[dateItem]
     ## count of all questions for a topic
     totcntQues = len(questionsForDate)
     ## questions for this topic
     topCntQues = qForTopic
     qPerDateTopic = float(topCntQues) / float(totcntQues)
     qPerDateTopic = round(qPerDateTopic, 3)
     trendPerTopicHolder.append(qPerDateTopic)
   print trendPerTopicHolder
   print '*'*75
