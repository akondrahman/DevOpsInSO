'''
March 24, 2017
esem dataset preparation
big and small
'''
import csv, os, numpy as np



def monthOfQues(dateStrParam):
    str2ret=''
    date_ = dateStrParam.split(' ')[0]
    ###print date_
    #This is the date format : 2014-06-11: yyyy-mm-dd
    if '/' in date_:
      mon   = date_.split('/')[1]
      year  = date_.split('/')[0]
    elif '-' in date_:
      mon   = date_.split('-')[1]
      year  = date_.split('-')[0]

    if(len(mon)==1):
        mon = '0' + mon

    str2ret = year + '-' + mon
    #print str2ret
    return str2ret


def getFullInfo(file_):
  fullContentDict={}
  with open(file_, 'rU') as f:
     reader_ = csv.reader(f)
     next(reader_)
     for row_ in reader_:
       qID              = row_[0]
       accID            = row_[1]
       createDate       = row_[4]
       formattedDate    = monthOfQues(createDate)
       viewCount        = row_[8]
       programmerID     = row_[10]
       if qID not in fullContentDict:
          fullContentDict[qID] = [accID, formattedDate, viewCount, programmerID]
  return fullContentDict
def getCategID(dirParam):
   categDict={}
   for csvFile in os.listdir(dirParam):
       if csvFile.endswith(".csv"):
          categ = os.path.basename(csvFile).split('.')[0]
          fullCSVFile = dirParam + csvFile
          with open(fullCSVFile, 'rU') as f:
               reader_ = csv.reader(f)
               for row_ in reader_:
                 if(len(row_)>0):
                   qID = row_[0]
                   if categ not in categDict:
                      categDict[categ] = [qID]
                   else:
                      categDict[categ] = categDict[categ] + [qID]
   return categDict




def getIDsFromSmallCategs(smallCategDict):
    list2ret=[]
    for key_, val_ in smallCategDict.items():
        for qID in val_:
            list2ret.append(qID)
    return list2ret




def constructFinalDataset(fullInfoDict, bigDict, smallDict):
   allSmallIDs = getIDsFromSmallCategs(smallDict)
   fullContentDict = {}
   '''
   handling big categ dict
   '''
   for categ_, questions_ in bigDict.items():
        questions_ = np.unique(questions_)
        for ques_ in questions_:
            if ((ques_ not in allSmallIDs) and (ques_ in fullInfoDict)):
                ques_details = fullInfoDict[ques_]
                ques_details = ques_details + [categ_]
                fullContentDict[ques_] = ques_details
   '''
   handling small  categ dict
   '''
   for categ_, questions_ in smallDict.items():
        questions_ = np.unique(questions_)
        for ques_ in questions_:
            if (ques_ in fullInfoDict):
                ques_details = fullInfoDict[ques_]
                ques_details = ques_details + [categ_]
                fullContentDict[ques_] = ques_details
   return fullContentDict




fullThing='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/ESEM/FullData_PuppetMarch21.csv'
bigCategDir='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/ESEM/big/'
smallCategDir='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/ESEM/small/'
fullThingDict = getFullInfo(fullThing)
#print fullThingDict
theBigCategDict   = getCategID(bigCategDir)
# for k_, v_ in theBigCategDict.items():
#     print "categ:{}, qs:{}".format(k_, len(v_))
print "Loaded files for big categories"
print "="*100
theSmallCategDict = getCategID(smallCategDir)
# for k_, v_ in theSmallCategDict.items():
#     print "categ:{}, qs:{}".format(k_, len(v_))
print "Loaded files for small categories"
print "="*100
'''
now calling the mega function
that will check for duplicates
and get the final dataset as dict
'''
completeDataset = constructFinalDataset(fullThingDict, theBigCategDict, theSmallCategDict)
print len(completeDataset)
print "="*100
