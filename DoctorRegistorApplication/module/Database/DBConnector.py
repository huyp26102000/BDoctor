import mysql.connector

class AppConnector():
    host = None
    user = None
    passwd = None
    database = None
    myconn = None
    cur = None
    
    def __init__(self, hostStr, userStr, passwdStr, databaseStr):
        self.host = hostStr
        self.user = userStr
        self.passwd = passwdStr
        self.database = databaseStr
    def connectTodataBase(self):
        self.myconn = mysql.connector.connect(host = self.host, user = self.user, passwd = self.passwd, database = self.database)
        self.cur = self.myconn.cursor()
    