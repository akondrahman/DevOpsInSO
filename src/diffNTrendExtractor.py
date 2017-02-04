



def giveConnection():
    import pymysql.cursors
    _host = "localhost"
    _user = "root"
    #password = "root"
    _password = "SrcML#2016"
    _database = "DevOpsInSO"
    # Connect to the database
    codealike_connection = pymysql.connect(host=_host,
                                 user=_user,
                                 password=_password,
                                 db=_database,
                                 cursorclass=pymysql.cursors.DictCursor)
    return codealike_connection

def getQuestionCount(window_size_param, switch_type_param):
 connection = giveConnection()
 try:
    with connection.cursor() as cursor:
     sql = "SELECT COUNT(`type`) FROM `FSE_window_context_switch`  WHERE `threshold`=%s AND `type`=%s GROUP BY `fileName`, `sessionID`, `windowID` ;"
     dataTuple=(window_size_param, switch_type_param)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()

 finally:
   connection.close()
 return result
