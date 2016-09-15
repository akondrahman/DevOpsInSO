# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 10:28:47 2016

@author: akond
"""

def giveConnection():
    import pymysql.cursors
    #_host = "localhost"
    _host = "127.0.0.1"    
    _user = "root"
    _password = "SrcML#2016"
    _database = "DevOpsInSO"
    _port=3306
    # Connect to the database
    codealike_connection = pymysql.connect(host=_host,
                                 user=_user,
                                 password=_password,
                                 db=_database,
                                 port=_port, 
                                 cursorclass=pymysql.cursors.DictCursor) 
    return codealike_connection 