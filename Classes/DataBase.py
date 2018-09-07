#conection with  DataBase

import MySQLdb



class DataBase():
    #constructor
    def __init__(self, password, db):
        self.db=db
        self.password=password

    def conection(self):

        return MySQLdb.connect(user='root',passwd=self.password,db=self.db)

    def transaction(self):
        cursor = self.conection().cursor()
        return cursor.execute(
            """INSERT INTO Users ( First_Name , Last_Name, Email, Phone, PIN, Birth_date) VALUES (?,?,?,?,?,?)""", (First_Name, Last_name, Email, Phone, PIN, Birth_date))

    def Match(self, data, PIN):
        cursor= self.conection().cursor()
        resp=cursor.execute("""SELECT First_Name from Users WHERE PIN = """+PIN)

        if resp > 0:
            r = cursor.fetchall()
        else:
            r = "NONE"

        return r

    def CreateUser(self, First_Name, Last_name, Email, Phone, PIN, Birth_date ):
        cursor = self.conection().cursor()
        if self.MatchEmail(Email) != True:
            return cursor.execute("""INSERT INTO Users ( First_Name , Last_Name, Email, Phone, PIN, Birth_date) VALUES (?,?,?,?,?,?)""",(First_Name, Last_name, Email, Phone, PIN, Birth_date ))

        else:
         return 'This user already exist'

    def MatchEmail(self, Email):
        return False


