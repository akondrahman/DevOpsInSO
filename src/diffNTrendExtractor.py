



def giveConnection():
    import pymysql.cursors
    _host = "localhost"
    _user = "devopsinso"
    #password = "root"
    _password = "NIRLIPTo@$99"
    _database = "DevOpsInSO"
    # Connect to the database
    codealike_connection = pymysql.connect(host=_host,
                                 user=_user,
                                 password=_password,
                                 db=_database,
                                 cursorclass=pymysql.cursors.DictCursor)
    return codealike_connection

def getQuestionCount(dateParam1, dateParam2, topicCntParam):
 connection = giveConnection()
 try:
    with connection.cursor() as cursor:
     sql = "SELECT COUNT(*) FROM `diffntrend` WHERE (`dateContent` LIKE" + dateParam1 + "or `dateContent` LIKE " + dateParam2 + " ) and `topIndCont`=" + topicCntParam + " ;"
     dataTuple=(window_size_param, switch_type_param)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()

 finally:
   connection.close()
 return result



lol = getQuestionCount('2016-06-%', '6/%/16', 20)
print lol
