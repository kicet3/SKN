#정적 페이지 웹 스크래핑  -> requests,beatuifulsoup
#정적 페이지 : 요청한 url에서 응답받은 html을 그대로 사용한 경우 (Server Side Rendering)
import os

os.chdir(os.path.dirname(__file__))
import sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from bs4 import BeautifulSoup


def web_request(url):
    response = requests.get(url)
    print(response)
    print(response.status_code)
    print(response.text)
    return response
# url = "https://www.naver.com"
# response = web_request(url)

with open('../html_sample.html','r',encoding='utf-8') as f:
    html = f.read()
bs = BeautifulSoup(html,'html.parser')
# print(bs)
# print(type(bs))

def test_find():
    tag = bs.find('li')
    print("tag!!",tag)
    print(type(tag))
    tags = bs.find_all('section',{'id':'section1'})
    print(tags)
    print(type(tags))


# test_find()

def test_selector():
    tag = bs.select_one('section#section2')
    tags = bs.select('.section-content')
    print(tags)
    print(type(tags))

def get_content():
    # bs.select()
    tags = bs.select('section#section2 li')

    for tag in tags:
        print(tag.text)

# get_content()#

def get_content2():
    #section1 h2 p
    htags = bs.select('section#section1 > h2')
    ptags = bs.select('section#section1 > p')
    for tag in htags:
        print(tag.text)
    for tag in ptags:
        print(tag.text)

def get_content3():
    section1_tag = bs.select_one('section#section1')
    h2_tag = section1_tag.select_one('h2')
    print(h2_tag)
    p_tags = section1_tag.select('p')
    print([p_tag.text for p_tag in p_tags ])
    children = section1_tag.findChildren()
    print(children)




get_content3()


# https://discord.com/oauth2/authorize?client_id=1340871817803464805&permissions=277025638464&integration_type=0&scope=bot


