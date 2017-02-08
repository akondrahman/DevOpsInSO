'''
Akond Rahman: Feb 07, 2017
'''
import os, csv, xlrd, collections, numpy as np
topicDict={1:'Puppet', 2:'Database', 3:'Network connection', 4:'Logging', 5:'Build artifacts',
           6:'Ruby on Rails', 7:'Java', 8:'IO', 9:'Containers', 10:'Web application',
           11:'SSH Authentication', 12:'System', 13:'Version Control', 14:'Deployment Environment', 15:'Web Services',
           16:'Openstack', 17:'Ansible', 18:'Package installation', 19:'Jenkins artifacts', 20:'Chef'
          }
def loadQsOfTopics(fileP):
    dictOfQs={}
    with open(fileP, 'rU') as f1:
      reader1 = csv.reader(f1)
      next(reader1, None)
      for row1 in reader1:
        topic_ = int(row1[2])
        ques_  = row1[4]
        if topic_ not in dictOfQs:
           dictOfQs[topic_] = [ ques_ ]
        else:
           dictOfQs[topic_] = dictOfQs[topic_] + [ ques_ ]
    return dictOfQs


def findTopicRels(q_dict_topic1, q_dict_topic2):
    strBuilder=''
    for top_1, que_1 in q_dict_topic1.iteritems():
      for top_2, que_2 in q_dict_topic2.iteritems():
         if((top_2 > top_1) ):
            topic1_name = topicDict[top_1]
            topic2_name = topicDict[top_2]
            intersect = set(que_1) & set(que_2)
            common_amongst_two = len(list(intersect))
            len_q1  = len(que_1)
            len_q2  = len(que_2)
            len_all = len_q1 + len_q2
            '''
            Here goes the metric
            '''
            topic_rel = (float(common_amongst_two) / float(len_all))*100
            print "TOPIC_REL among Topic#{} and Topic#{} is:{}%".format(topic1_name, topic2_name, topic_rel)
            print "*"*50
            strBuilder = strBuilder +  str(topic_rel) + ','
         else:
            strBuilder = strBuilder +   ','
      strBuilder = strBuilder + '\n'
    return strBuilder


def dumpContentIntoFile(strP, fileP):
  fileToWrite = open( fileP, 'w');
  fileToWrite.write(strP );
  fileToWrite.close()
  return str(os.stat(fileP).st_size)





fileName='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq1/you_are_never_done/Title_TrendInp.csv'
dumpFiileName='/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq1/you_are_never_done/TopicRel.csv'
QDict=loadQsOfTopics(fileName)
# for top_, q_ in QDict.iteritems():
#     print "Topic:{}, ques. count:{}".format(top_, len(q_))
#     print "="*100
QDict = collections.OrderedDict(sorted(QDict.items()))
strs_ = findTopicRels(QDict, QDict)
staus_ = dumpContentIntoFile(strs_, dumpFiileName)
print "Dumped a file of {} bytes".format(staus_)
