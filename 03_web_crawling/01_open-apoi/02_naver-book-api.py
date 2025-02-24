import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import urllib.parse
import urllib.request
import json
from db_connector import connect_to_mysql
from dotenv import load_dotenv
load_dotenv()
#API KEY
client_id = os.getenv("NAVER_API_CLIENT")
client_secret = os.getenv("NAVER_API_SECRET")


baseConfig = {
    'user':'snowfall',
    'password':'Ikillyou2@',
    'host':'127.0.0.1',
    'database':'bookdb',
    'raise_on_warnings':True,
}


def dbInsert(insertData):
    connection = connect_to_mysql(baseConfig)

    sql = "INSERT INTO naver_book (book_title,book_image,author,publisher,isbn,book_description,pub_date) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    if connection.is_connected():
        #SQL 수행을 위한 cursor
        with connection.cursor() as cursor:
            cursor.execute(sql,insertData)
            connection.commit()
    #커서 및 연결 객체 종료 및 반납            
    connection.close()

def naverBookAPI(searchItem):
    searchText = urllib.parse.quote(searchItem)
    #URL 및 헤더 설정
    url = "https://openapi.naver.com/v1/search/book.json?query=" + searchText+'&display=60'

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        #API 요청 및 결과 값 JSON으로 변경
        response_body = response.read()
        response_body = json.loads(response_body)
        book_list = response_body["items"]
        return book_list
    else:
        print("Error Code:" + rescode)

def main():
    # 검색어 입력
    bookList = naverBookAPI('점심')
    #받은 정보 만큼 SQL 수행하기 위해 반복문 수행
    for bookInfo in bookList:
        values = (bookInfo["title"],bookInfo["image"],bookInfo["author"],bookInfo["publisher"],str(bookInfo["isbn"]),bookInfo["description"],bookInfo["pubdate"])
        dbInsert(values)

  
main()
