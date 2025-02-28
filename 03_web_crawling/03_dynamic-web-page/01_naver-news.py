# 동적 페이지 웹 스크래핑 <- selenium
# 동적 페이지 : 요청한 URL에서 응답받은 HTML 안의 JS를 실행해 HTML을

#Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options() 
chrome_options.add_argument("--disable-gpu") 
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# text = input('검색어를 입력 : ')                                       
# 1. 크롬 실행
path = './chromedriver.exe'
service = Service(path)
driver = webdriver.Chrome()

# 2. 특정 URL 접근
# driver.get(f'https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={text}')
# driver.get(f'https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=chat+gpt')
driver.get(f'https://www.naver.com')
# 3. 검색 처리
search_box = driver.find_element(By.ID,"query")
search_box.send_keys('chat gpt')
search_box.send_keys(Keys.RETURN)
time.sleep(1)
news_tab = driver.find_element(By.XPATH, "//a[@role='tab' and contains(., '뉴스')]")
news_tab.click()

# 4. 스크롤 처리
for _ in range(5):
    body = driver.find_element(By.TAG_NAME,'body')
    body.send_keys(Keys.END)
    time.sleep(1)
# 5. 특정 요소에 접근
news_contents_elems = driver.find_elements(By.CSS_SELECTOR,"div.news_contents")
print(len(news_contents_elems))
for news_contents_elem in news_contents_elems:
    a_tag = news_contents_elem.find_element(By.CSS_SELECTOR,'a.news_tit')
    title = a_tag.text
    href = a_tag.get_attribute('href')
    print(title ,'|',href)
time.sleep(5)
driver.quit()


