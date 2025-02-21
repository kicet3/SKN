import mysql.connector

config = {
    'user':'snowfall',
    'password':'Ikillyou2@',
    'host':'127.0.0.1',
    'database':'menudb',
    'raise_on_warnings':True,
}


cnx = mysql.connector.connect(**config)

sql = "UPDATE tbl_menu SET menu_name = %s WHERE menu_code = %s"
data =('볶음밥','1')
cursor = cnx.cursor()
result = cursor.execute(sql,data)
print(f'{cursor.rowcount}개의 행을 변경하였습니다.')

cnx.commit()    
cnx.close()

