import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
from urllib.request import urlretrieve
os.chdir(os.path.dirname(__file__))

#스크랩한 뉴스 정보를 담은 NewsEntry Class
class NewsEntry:
    def __init__(self,title,href,img_path):
        self.title = title
        self.href = href
        self.img_path = img_path
    def __repr__(self):
        return f'NewsEntry<title={self.title}, href={self.href}, img_path={self.img_path}>'


keyword = input("뉴스 키워드 검색 : ")
url = f"https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={keyword}"

response = requests.get(url)

html = response.text

bs = BeautifulSoup(html,'html.parser')

news_contents = bs.select('div.news_contents')

# print(len(news_contents))
news_list = []
for i,news_content in enumerate(news_contents):
    a_tag = news_content.select_one('a.news_tit')
    title = a_tag.text
    href = a_tag['href']
    img_tag = news_content.select_one('img.thumb')
    img_lazysrc = img_tag['data-lazysrc']
    if img_lazysrc.startswith("http"):
        img_dir = "/Users/link/Documents/GitHub/SKN/03_web_crawling/02_static_web-apge/images"
        today = datetime.now().strftime('%y%m%d')
        filename = f'{img_dir}/{today}_{i}.jpg'
        urlretrieve(img_lazysrc,filename)
    news_entry = NewsEntry(title,href,filename)
    news_list.append(news_entry)
# 결과 출력
for news in news_list:
    print(news)
        