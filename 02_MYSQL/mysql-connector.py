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
        result = cursor.execute("SELECT * FROM tbl_menu LIMIT 5")
        rows = cursor.fetchall()
        for rows in rows:
            print(rows)
    cnx.close()
else:
    print("Connection Fail")
