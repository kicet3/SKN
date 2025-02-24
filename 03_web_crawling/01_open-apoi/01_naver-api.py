import os
import sys
import urllib.parse
import urllib.request
from dotenv import load_dotenv
load_dotenv()
client_id = os.getenv("NAVER_API_CLIENT")
client_secret = os.getenv("NAVER_API_SECRET")

searchText = urllib.parse.quote('오늘 점심')

url = "https://openapi.naver.com/v1/search/blog.json?query=" + searchText

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
