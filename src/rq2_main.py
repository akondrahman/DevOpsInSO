# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 09:48:23 2016

@author: akond
"""



import rq2_utility 
file2save_prefix = "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/final_rq2."
header2dump="Score_Q,VCount_Q,AnsCount_Q,ComCount_Q,FavCount_Q,Score_A"
ans_unix_file = "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/LOCKED_ANS/ans_unix_all.csv"
ans_su_file   = "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/LOCKED_ANS/ans_super_user_all.csv"
ans_so_file   = "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/LOCKED_ANS/ans_stack_overflow_all.csv" 
ans_sf_file   = "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/LOCKED_ANS/ans_server_fault_all.csv"
ans_au_file   = "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/LOCKED_ANS/ans_ask_ubuntu_all.csv"


#### Q&A site: unix.stackexchange.com
#dict_ans_unix = rq2_utility.getAnsDictFromCSV(ans_unix_file)
#srcName="unix"
#dict_que_unix = rq2_utility.getFormattedRecordOfAnswer(srcName)
#unix_rep_as_lis = rq2_utility.createRQ2Report(dict_que_unix, dict_ans_unix)
#print "Expected answers in UNIX: ", len(dict_que_unix)
#print "Matched records for UNIX: ", len(dict_ans_unix)
##print "Detail fo the matched reocrds: \n" unix_rep_as_lis, 
#file2save= file2save_prefix+srcName+".csv"
#dump_status = rq2_utility.dumpFinalReport(unix_rep_as_lis, header2dump, file2save)
#print "Dumped the full report in CSV file of {} bytes".format(dump_status)
#print "="*50
#
#
#
#### Q&A site: superuser.stackexchange.com
#dict_ans_s_u_ = rq2_utility.getAnsDictFromCSV(ans_su_file)
#srcName="su"
#dict_que_su   = rq2_utility.getFormattedRecordOfAnswer(srcName)
#su_rep_as_lis = rq2_utility.createRQ2Report(dict_que_su, dict_ans_s_u_)
#print "Expected answers in super user: ", len(dict_que_su)
#print "Matched records for super user: ", len(dict_ans_s_u_)
##print "Detail fo the matched reocrds: \n" su_rep_as_lis, 
#file2save= file2save_prefix+srcName+".csv"
#dump_status = rq2_utility.dumpFinalReport(su_rep_as_lis, header2dump, file2save)
#print "Dumped the full report in CSV file of {} bytes".format(dump_status)
#print "="*50
#
#
#
#### Q&A site: server.fault.stackexchange.com
#dict_ans_s_f_ = rq2_utility.getAnsDictFromCSV(ans_sf_file)
#srcName ="sf" 
#dict_que_sf_  = rq2_utility.getFormattedRecordOfAnswer(srcName)
#sf_rep_as_lis = rq2_utility.createRQ2Report(dict_que_sf_, dict_ans_s_f_)
#print "Expected answers in server fault: ", len(dict_que_sf_)
#print "Matched records for server fault: ", len(dict_ans_s_f_)
##print "Detail fo the matched reocrds: \n" sf_rep_as_lis, 
#file2save= file2save_prefix+srcName+".csv"
#dump_status = rq2_utility.dumpFinalReport(sf_rep_as_lis, header2dump, file2save)
#print "Dumped the full report in CSV file of {} bytes".format(dump_status)
#print "="*50
#
#
#
######## Q&A site anme: askububtu.stackexhange.com  #######
#dict_ans_au_  = rq2_utility.getAnsDictFromCSV(ans_au_file)
#srcName="au"
#dict_que_au   = rq2_utility.getFormattedRecordOfAnswer(srcName)
#au_rep_as_lis = rq2_utility.createRQ2Report(dict_que_au, dict_ans_au_)
#print "Expected answers in ask ubuntu: ", len(dict_que_au)
#print "Matched records for ask ubuntu: ", len(au_rep_as_lis)
##print "Detail fo the matched reocrds: \n" , au_rep_as_lis
#file2save= file2save_prefix+srcName+".csv"
#dump_status = rq2_utility.dumpFinalReport(au_rep_as_lis, header2dump, file2save)
#print "Dumped the full report in CSV file of {} bytes".format(dump_status)
#print "="*50



####### Q&A site anme: stackoverflow.stackexhange.com  #######
#dict_ans_so_  = rq2_utility.getAnsDictFromCSV(ans_so_file)
#srcName="so"
##dict_que_so   = rq2_utility.getFormattedRecordOfAnswer(srcName)
#extra_file_name_for_so = "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/rq2_all_so.csv"
#dict_que_so   = rq2_utility.getExtraFormattedRecordOfAnswer(extra_file_name_for_so)
#### extra rae for stupid db connections 
#so_rep_as_lis = rq2_utility.createRQ2Report(dict_que_so, dict_ans_so_)
#print "Expected answers in stack overflow: ", len(dict_que_so)
#print "Matched records for stack overflow: ", len(so_rep_as_lis)
##print "Detail fo the matched reocrds: \n" , so_rep_as_lis
#file2save= file2save_prefix+srcName+".csv"
#dump_status = rq2_utility.dumpFinalReport(so_rep_as_lis, header2dump, file2save)
#print "Dumped the full report in CSV file of {} bytes".format(dump_status)
#print "="*50

################## ###############