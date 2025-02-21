import mysql.connector

config = {
    'user':'snowfall',
    'password':'Ikillyou2@',
    'host':'127.0.0.1',
    'database':'menudb',
    'raise_on_warnings':True,
}


cnx = mysql.connector.connect(**config)

sql = "INSERT INTO tbl_menu (menu_name,menu_price,category_code,orderable_status) VALUES(%s,%s,%s,%s)"
data = ("새우깡매운탕",15000,4,"Y")
cursor = cnx.cursor()
result = cursor.execute(sql,data)
print(f'{cursor.rowcount}개의 행을 삽입하였습니다.')

cnx.commit()    
cnx.close()

