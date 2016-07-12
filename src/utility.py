from contextlib import contextmanager
import numpy as np, os

def findStringInPost(bodStringParam):
  flag_ = False
  #elems = ['gameshark', 'reconstruction', 'bitsavers']
  elems = ['AWS' , 'AWS CodeDeploy' , 'AWS OpsWorks' , 'Agile management' ,'Ansible',
 'Ansible Cookbooks', 'Ansible playbooks', 'Arcadia',
 'Automated infrastructure testing', 'Azure', 'Azure Stack', 'Bcfg2', 'Bento',
 'Boto', 'CFEngine', 'Capistrano', 'Cfg4j', 'Chef', 'Chef Solo', 'Chef recipes',
 'Chef spec', 'Cisco Unified Computing System', 'CliqR', 'Cloud',
 'Cloud Deployment Projects', 'Cloud formation', 'Cloud management',
 'Cloudbank', 'Composable infrastructure', 'Configuration code', 'Container',
 'Continuous Delivery', 'Continuous Deployment', 'Continuous testing',
 'Cookbook', 'DevOps', 'Docker', 'Fabric', 'HPE Discover', 'HPE Oneview',
 'HPE Synergy', 'Infrastructure', 'Infrastructure as code', 'Intoto',
 'JFrog Mission Control', 'JSON', 'Jiml', 'Job DSL', 'Job DSL Language',
 'Job DSL Plugin', 'Kitchen', 'Knife', 'Kubernetes', 'Manifest', 'NS1',
 'Octopus Deploy', 'OpsCode', 'OpsCode Chef', 'Orchestration', 'Otter', 'Packer',
 'Parameterized classes', 'PowerShell Desired State Configuration',
 'Programmable Infrastructure', 'Programmable infrastructure', 'Provisioning',
 'Puppet', 'Puppet modules', 'SaltStack', 'Script', 'Scripts', 'Server spec',
 'Snowflake deployment', 'Terraform', 'VMWare NSX', 'VMWare Photon', 'Vagrant',
 'XML', 'Yaml', 'amazon web service', 'configuration', 'deploy', 'mruby',
 'openshift', 'playbook', 'powershell', 'shell', 'solo', 'vmware',
 'amazon web services', 'jenkins', 'manifest', 'ibm bluemix', 'bluemix' ,
 'recipe', 'recipe', 'bamboo']

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
    #print list_ret
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
    #print list_ret
    return list_ret
