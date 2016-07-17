from contextlib import contextmanager
import numpy as np, os

def findStringInPost(bodStringParam):
  flag_ = False
  #elems = ['gameshark', 'reconstruction', 'bitsavers']
  elems = ['Ansible'           , 'openstack'         , 'CFEngine'   , 'Chef'       ,
           'Docker'            , 'Capistrano'        , 'Kubernetes' ,
           'Puppet'            , 'SaltStack'         , 'Vagrant'    , 'ibm bluemix', 
           'amazon web service', 'openshift'         , 'jenkins'   
           ]

  formatted_body_str = bodStringParam.lower()
  #print "toatal keywords: ", len(elems)
  for elem in elems:
    elem_lower = elem.lower()
    if elem_lower in formatted_body_str:
      flag_ = True
      #print "Matched elem", elem
  return flag_



@contextmanager
def duration():
  import time
  t_old = time.time()
  yield
  t_new = time.time()
  print("\n" + "-" * 100)
  print("# Runtime: %.3f secs" % (t_new-t_old))


def readCSVForKeywords(fileNameParam):
  import csv
  kwList = []
  with open(fileNameParam, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
         for elems in row:
             if elems != '':
               kwList.append(elems)
  return kwList

def getTags(fileNameParam):
    tagList = []
    f_ = open(fileNameParam)
    for line in iter(f_):
       if line!='NA':
           extracted_tags=line.split('>')
           for tag in extracted_tags:
               if '<' in tag:
                 formatted_tag = tag.split('<')[1]
                 tagList.append(formatted_tag)
    f_.close()
    list_ret = np.unique(tagList)
    print "Total tags:", len(list_ret)
    return list_ret
def findStringInTag(tagP, strToSearchParam):
   flagToRet = False
   if tagP in strToSearchParam:
     flagToRet = True
   return flagToRet
def dumpContentIntoFile(strP, fileP):
  fileToWrite = open( fileP, 'w');
  fileToWrite.write(strP );
  fileToWrite.close()
  return str(os.stat(fileP).st_size)

def preprocesstags(rawTagsParam):
  tagList = []  
  if (len(rawTagsParam) > 0):
    rawTags = rawTagsParam.split('>')
    for raw_tag in rawTags:
      if '<' in raw_tag: 
        formatted_tag = raw_tag.split('<')[1]
        tagList.append(formatted_tag)          
  return tagList
def getFormattedTags(fileNameParam):
    tagList = []
    f_ = open(fileNameParam)
    for line in iter(f_):
       if line!='':
          if '\n' in line:
              line = line.strip('\n')
              tagList.append(line)
    f_.close()
    list_ret = np.unique(tagList)
    print "Total formatted tags:", len(list_ret)
    return list_ret




#def findStringInAllTags(allTagsParam, tag_unicoded_str):
#  flagToRet = False     
#  comaprer_tags = preprocesstags(tag_unicoded_str)
#  comapree_tags =  allTagsParam
#  res = set(comaprer_tags) & set(comapree_tags)
#  if len(res) > 0: 
#    flagToRet = True 
#    print "comparer ={}, comparee={}, res={}".format(comaprer_tags, comapree_tags, res)
#  return flagToRet      

# phase-1
# elems = ['AWS' , 'AWS CodeDeploy' , 'AWS OpsWorks' , 'Agile management' ,'Ansible',
# 'Ansible Cookbooks', 'Ansible playbooks', 'Arcadia',
# 'Automated infrastructure testing', 'Azure', 'Azure Stack', 'Bcfg2', 'Bento',
# 'Boto', 'CFEngine', 'Capistrano', 'Cfg4j', 'Chef', 'Chef Solo', 'Chef recipes',
# 'Chef spec', 'Cisco Unified Computing System', 'CliqR', 'Cloud',
# 'Cloud Deployment Projects', 'Cloud formation', 'Cloud management',
# 'Cloudbank', 'Composable infrastructure', 'Configuration code', 'Container',
# 'Continuous Delivery', 'Continuous Deployment', 'Continuous testing',
# 'Cookbook', 'DevOps', 'Docker', 'Fabric', 'HPE Discover', 'HPE Oneview',
# 'HPE Synergy', 'Infrastructure', 'Infrastructure as code', 'Intoto',
# 'JFrog Mission Control', 'JSON', 'Jiml', 'Job DSL', 'Job DSL Language',
# 'Job DSL Plugin', 'Kitchen', 'Knife', 'Kubernetes', 'Manifest', 'NS1',
# 'Octopus Deploy', 'OpsCode', 'OpsCode Chef', 'Orchestration', 'Otter', 'Packer',
# 'Parameterized classes', 'PowerShell Desired State Configuration',
# 'Programmable Infrastructure', 'Programmable infrastructure', 'Provisioning',
# 'Puppet', 'Puppet modules', 'SaltStack', 'Script', 'Scripts', 'Server spec',
# 'Snowflake deployment', 'Terraform', 'VMWare NSX', 'VMWare Photon', 'Vagrant',
# 'XML', 'Yaml', 'amazon web service', 'configuration', 'deploy', 'mruby',
# 'openshift', 'playbook', 'powershell', 'shell', 'solo', 'vmware',
# 'amazon web services', 'jenkins', 'manifest', 'ibm bluemix', 'bluemix' ,
# 'recipe', 'recipe', 'bamboo']


# phase-2
# elems = ['AWS' , 'AWS CodeDeploy' , 'AWS OpsWorks' , 'Agile management' ,'Ansible',
# 'Ansible Cookbook', 'Ansible playbook', 'Azure', 'Azure Stack', 'CFEngine', 'Capistrano',
# 'Chef', 'Chef Solo', 'Chef recipes',
# 'Chef spec', 'Cloud',
# 'Cloud Deployment Projects', 'Cloudformation', 'Cloudmanagement',
# 'Cloudbank', 'Composable infrastructure', 'Container',
# 'Continuous Delivery', 'Continuous Deployment', 'Continuous testing',
# 'Cookbook', 'DevOps', 'Docker', 'HPE Discover', 'HPE Oneview',
# 'HPE Synergy', 'Infrastructure as code', 'Jiml', 'Job DSL Language',
# 'Job DSL Plugin', 'Kubernetes', 'Manifest',
# 'Octopus Deploy', 'OpsCode', 'OpsCode Chef', 'Orchestration', 'Packer',
# 'Parameterized class', 'Programmable infrastructure', 'Provisioning',
# 'Puppet', 'Puppet modules', 'SaltStack', 'Script', 'Server spec',
# 'Snowflake deployment', 'VMWare NSX', 'VMWare Photon', 'Vagrant',
# 'yml', 'Yaml', 'amazon web service', 'openstack',
# 'openshift', 'playbook', 'powershell', 'shell',
# 'jenkins', 'manifest', 'ibm bluemix', 'bamboo']


#phase-3
# elems = ['AWS' , 'AWS CodeDeploy' , 'AWS OpsWorks' , 'Ansible',
# 'Ansible Cookbook', 'Ansible playbook', 'Azure', 'Azure Stack', 'CFEngine', 'Capistrano',
# 'Chef', 'Chef Solo', 'Chef recipes',
# 'Chef spec', 'Cloudformation', 'Cloudmanagement',
# 'Cloudbank', 'Container',
# 'Continuous Delivery', 'Continuous Deployment', 'Continuous testing',
# 'Cookbook', 'DevOps', 'Docker', 'Jiml', 'Job DSL Language',
# 'Job DSL Plugin', 'Kubernetes', 'Manifest',
# 'OpsCode', 'OpsCode Chef', 'Puppet', 'SaltStack',
# 'Vagrant', 'yml', 'Yaml', 'amazon web service', 'openstack',
# 'openshift', 'playbook',
# 'jenkins', 'manifest', 'ibm bluemix', 'bamboo']


#phase-4
# elems = ['AWS' , 'AWS CodeDeploy' , 'AWS OpsWorks' , 'Ansible',
# 'Azure', 'CFEngine', 'Chef', 'Cloudformation', 'Container',
# 'Continuous Delivery', 'Continuous Deployment',
# 'DevOps', 'Docker', 'Jiml', 'Job DSL',
# 'Kubernetes', 'OpsCode', 'Puppet', 'SaltStack',
# 'Vagrant', 'yml', 'Yaml', 'amazon web service', 'openstack',
# 'openshift', 'jenkins', 'ibm bluemix']

#phase-5
#  elems = ['Ansible'           , 'Azure'             , 'CFEngine'  , 'Chef'      ,
#           'Docker'            , 'Jiml'              , 'Job DSL'   , 'Kubernetes',
#           'Puppet'            , 'SaltStack'         , 'Vagrant'   , 'Yaml'      , 
#           'amazon web service', 'openshift'         , 'jenkins'   , 'ibm bluemix'
#           ]

#phase-6
#  elems = ['Ansible'           , 'Azure'             , 'CFEngine'  , 'Chef'       ,
#           'Docker'            , 'Capistrano'        , 'Job DSL'   , 'Kubernetes' ,
#           'Puppet'            , 'SaltStack'         , 'Vagrant'   , 'ibm bluemix', 
#           'amazon web service', 'openshift'         , 'jenkins'   
#           ]

def getTagsFromFormattedFile(fileNameParam):
  import csv
  tagList = []
  with open(fileNameParam, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
         for elems in row:
             if elems != '':
               tagList.append(elems)
  unique_tag_list = np.unique(tagList)
  print "Total tags to look for ", len (unique_tag_list)             
  return tagList

def getAllExistingTagsinSO(allTagsinSOParam): 
  import csv
  tagList = []
  with open(allTagsinSOParam, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
      if row[1] != '':
        tagList.append(row[1])
  return tagList    


def writeTagsToFile(inFileParam, outFileParam): 
  theTags = getTags(inFileParam) 
  current_tags_in_so = getAllExistingTagsinSO('AllTagsinSO.csv')
  str_ = ''  
  for tag_ in theTags:
    if tag_ in current_tags_in_so:  
      str_ = str_ + tag_ + ',' + '\n'        
  sta_ = dumpContentIntoFile(str_, outFileParam)
  return sta_   
if __name__ == "__main__":
  dirName='stackoverflow.com-Posts'
  inFile =  dirName +  '.matching_tags.txt'  
  status_ = writeTagsToFile(inFile, 'allTagsOfInterest.txt')  
  print "Dumped-a-file-of-{}-bytes".format(status_)  