'''
Akond Rahman: Dec 01, 2016
'''
import os, csv, numpy as np, collections
def dumpContentIntoFile(strP, fileP):
  fileToWrite = open( fileP, 'w');
  fileToWrite.write(strP );
  fileToWrite.close()
  return str(os.stat(fileP).st_size)

file2write="/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/QCOuntAndDate.csv"
str2dump=""
file2read="/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq1/you_are_never_done/_TrendInp.csv"

def extractMonthWiseQCount(fileP):
  dateAndQHolder={}
  with open(fileP, 'rU') as f1:
    reader1 = csv.reader(f1)
    next(reader1, None)
    for row_ in reader1:
      dateOfQues = row_[1]
      #print dateOfQues
      IDOfQues   = row_[0]
      if ('/' in dateOfQues):
        splittedDate = dateOfQues.split('/')
        monthOfQues  = splittedDate[0]
        if (len(monthOfQues)==1):
          monthOfQues = "0" + monthOfQues
        yearOfQues   = splittedDate[2]
        date2Use     = "20" + yearOfQues + '-' + monthOfQues
      elif ('-' in dateOfQues):
        splittedDate = dateOfQues.split('-')
        yearOfQues   = splittedDate[0]
        monthOfQues  = splittedDate[1]
        date2Use     = yearOfQues + "-" + monthOfQues
      #print date2Use
      if date2Use not in dateAndQHolder:
        dateAndQHolder[date2Use] = [ IDOfQues ]
      else:
        dateAndQHolder[date2Use] = dateAndQHolder[date2Use] + [ IDOfQues ]
  #print "dates:", len(dateAndQHolder)
  return dateAndQHolder


dates_ = extractMonthWiseQCount(file2read)
datesWithUniqueQs={}
for k_, v_ in dates_.iteritems():
   uniqueQs = np.unique(v_)
   datesWithUniqueQs[k_] = uniqueQs
#print "="*100



datesWithUniqueQs = collections.OrderedDict(sorted(datesWithUniqueQs.items()))
for uniqueDate, uniqueQ in datesWithUniqueQs.iteritems():
   print "unique date:{}, unique qCount:{}".format(uniqueDate, len(uniqueQ))
   str2dump = str2dump + uniqueDate + "," + str(len(uniqueQ)) + "\n"

st_ = dumpContentIntoFile(str2dump, file2write)
print "Dumped a file of {} bytes".format(st_)
