import mysql.connector

config = {
    'user':'snowfall',
    'password':'Ikillyou2@',
    'host':'127.0.0.1',
    'database':'menudb',
    'raise_on_warnings':True,
}

# menu_code가 100번이상인 메뉴 삭제

cnx = mysql.connector.connect(**config)

sql = "DELETE FROM tbl_menu WHERE menu_code>=100"
cursor = cnx.cursor()
result = cursor.execute(sql)
print(f'{cursor.rowcount}개의 행을 삭제 했습니다.')


cnx.commit()    
cnx.close()
