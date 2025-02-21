import mysql.connector

config = {
    'user':'snowfall',
    'password':'Ikillyou2@',
    'host':'127.0.0.1',
    'database':'menudb',
    'raise_on_warnings':True,
}


cnx = mysql.connector.connect(**config)

if cnx and cnx.is_connected():
    with cnx.cursor() as cursor:
        cursor.execute("SELECT menu_code,menu_name,menu_price FROM tbl_menu")
        rows = cursor.fetchall()
        for row in rows: #한 행의 결과
            print('menuCode:',row[0],'/','menucode:',row[1],'/','menuprice:',row[2])
    cnx.close()
else:
    print("Connection Fail")
