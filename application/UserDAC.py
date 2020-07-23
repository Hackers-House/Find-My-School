import pyodbc
from config import Config
def GetConnection():
        cxn=pyodbc.connect(driver=Config.Driver,server=Config.Server,PORT=1433, user=Config.User, password=Config.Password, database=Config.Database,TDS_VERSION=7.2)
        return cxn
def GetIndex():
    con=GetConnection()
    cur = con.cursor()
    cur.execute("SELECT userid FROM UserDetails ORDER BY userid DESC")
    data = cur.fetchone()
    cur.close()
    if data ==None:
        return 0
    return int(data[0])
def GetTable():
    con=GetConnection()
    cur = con.cursor()
    cur.execute("SELECT * FROM UserDetails")
    data = cur.fetchone()
    cur.close()
    return data
def SetData(idd,name,email,git,link,tech):
    con=GetConnection()
    cur = con.cursor()
    cur.execute('insert into UserDetails(userid,username,email,Github_url,linkdln_Url,Technologies) VALUES(?,?,?,?,?,?)',idd,name,email,git,link,tech)
    cur.commit()
    cur.close()
    print('row with user id '+str(idd)+' inserted sucessfully')
print(GetIndex())