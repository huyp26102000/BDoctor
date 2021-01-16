import mysql.connector
import uuid 
from ..UtilityFunction import *
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
    def registorAccount(self, doctorObject):
        uuID = str(uuid.uuid1())
        # Get 
        drName = str(doctorObject.familyName) + ' ' + str(doctorObject.lastName)
        AccUsername = str(getAccountName(drName))
        nextAccID = self.getNextAccountNumber(AccUsername)
        AccUsername+= str(nextAccID)

        tempPassword = getRandomText()

        self.pushAccountInfor(uuID, AccUsername, getCrytoPassword(tempPassword), 1)
        self.pushInitAccountInfor(uuID, AccUsername, tempPassword)
    def pushAccountInfor(self, uuid, AccUsername, AccPassword, role):
        sqlAccountInfor = ("insert into bdoctordb.accountinfor(UUID, username, password, role) "
                        "values (%s, %s, %s, %s)")
        AccountInforVal = (uuid, AccUsername, AccPassword, role)
        try:
            #inserting the values into the table
            self.cur.execute(sqlAccountInfor, AccountInforVal)
            #commit the transaction
            self.myconn.commit()
        except:
            self.myconn.rollback()
        print(self.cur.rowcount,"Account record uploaded!")
    def pushInitAccountInfor(self, uuid, AccUsername, AccPassword):
        sqlAccountInfor = ("insert into bdoctordb.initAccount(UUID, username, password, changingstatus) "
                        "values (%s, %s, %s, %s)")
        AccountInforVal = (uuid, AccUsername, AccPassword, None)
        try:
            #inserting the values into the table
            self.cur.execute(sqlAccountInfor, AccountInforVal)
            #commit the transaction
            self.myconn.commit()
        except:
            self.myconn.rollback()
        print(self.cur.rowcount,"Initiation Account record uploaded!")
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
# DBConnector.pushAccountInfor("abc", "HuyP", "abc@123abc", 0)
# DBConnector.getNextAccountNumber("huyp")