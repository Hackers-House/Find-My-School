import pyodbc
import pandas as pd
def GetConnection():
        cxn=pyodbc.connect(driver='ODBC Driver 17 for SQL Server',server='Anush', user='sa', password='Bu1ssnessman', database='LCH')
        return cxn

def GetTable():
    con=GetConnection()
    cur = con.cursor()
    cur.execute("SELECT * FROM UserDetails")
    data = cur.fetchall()
    cur.close()
    return data
def SetData(obj):
    con=GetConnection()
    cur = con.cursor()
    cur.execute('insert into User_Details (username,email,Guthub_url,linkdln_Url,Technologies) VALUES(?,?)',obj.name,obj.email,obj.git,obj.link,obj.tech)
    data = cur.fetchall()
    cur.close()
    return data
