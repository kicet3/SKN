import sqlite3 as db

connect = db.connect('temp.db')

cursor = connect.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS CHAT(name,chatInfo)")
connect.commit()

def insertData(user,chatData):
    cursor.execute("INSERT INTO CHAT VALUES(?,?)",(user,chatData))
    connect.commit()

def getData(user):
    cursor.execute("SELECT * FROM CHAT WHERE name=?",(user))
    connect.commit()
