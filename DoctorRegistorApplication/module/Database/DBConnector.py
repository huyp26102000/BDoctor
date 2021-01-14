import mysql.connector
import uuid
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
    # Example guide: DBConnector.pushAccountInfor("HuyP4", "abc@123abc", 0)
    def pushAccountInfor(self, id, AccUsername, AccPassword, role):
        nextAccID = self.getNextAccountNumber(str(AccUsername))
        AccUsername+=str(nextAccID)
        sqlAccountInfor = ("insert into bdoctordb.accountInfor(ID, username, password, role) "
                        "values (%s, %s, %s, %s)")
        AccountInforVal = (None, AccUsername, AccPassword, role)
        try:
            #inserting the values into the table
            self.cur.execute(sqlAccountInfor, AccountInforVal)
            #commit the transaction
            self.myconn.commit()
        except:
            self.myconn.rollback()
        print(self.cur.rowcount,"Account record uploaded!")
    def pushDoctorInfor(self, doctorProfileObj):
        sqlDoctorInfor = ("insert into bdoctordb.accountInfor(ID, username, password, role) "
                        "values (%s, %s, %s, %s)")
        DoctorInforInforVal = (None, AccUsername, AccPassword, role)
        try:
            #inserting the values into the table
            self.cur.execute(sqlDoctorInfor, DoctorInforInforVal)
            #commit the transaction
            self.myconn.commit()
        except:
            self.myconn.rollback()
        print(self.cur.rowcount,"Account record uploaded!")


    def getNextAccountNumber(self, AccUsername):
        AccUsername = AccUsername.lower()
        count = 0
        self.cur.execute("SELECT username FROM bdoctordb.accountinfor")
        allRecord = self.cur.fetchall()
        for tmp in allRecord:
            tmpStr = str(tmp)
            tmpStr = tmpStr.lower()
            if(tmpStr.__contains__(AccUsername)):
                count+=1
        count+=1
        return count
# DBConnector = AppConnector("localhost", "root", "lemon", "bdoctordb")
# DBConnector.connectTodataBase()
# DBConnector.pushAccountInfor("HuyP", "abc@123abc", 0)
# DBConnector.getNextAccountNumber("huyp")