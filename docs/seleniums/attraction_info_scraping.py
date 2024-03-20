# * 웹 크롤링 동작
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
import time
# ChromeDriver 실행

from selenium.webdriver.chrome.options import Options

from pymongo import MongoClient
mongoClient = MongoClient("mongodb://192.168.10.240:27017/AI_LKJ")

# database 연결
database = mongoClient["AI_LKJ"]

# collection 작업
attraction_search_info_collection = database['attraction_search_info']
attraction_search_info_collection
attraction_name_dict=attraction_search_info_collection.find({}, {'_id':0,'attraction_name': 1})
# attraction_search_info_collection.update_many({"attraction_name" :attraction_name_list[0]},{"$set" : {"attraction_img":"","attraction_link":""}})
# collection.delete_many({})
# Chrome 브라우저 옵션 생성
attraction_name_list = []
for attraction_element in attraction_name_dict:
    attraction_name_list.append(attraction_element['attraction_name'])
chrome_options = Options()

# User-Agent 설정
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

# WebDriver 생성
webdriver_manager_dricetory = ChromeDriverManager().install()

browser = webdriver.Chrome(service = ChromeService(webdriver_manager_directory), options=chrome_options)                        # - chrome browser 열기

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

pass
browser.get("https://korean.visitkorea.or.kr/search/search_list.do?keyword=")                                     # - 주소 입력

                                                    # - 가능 여부에 대한 OK 받음
pass
time.sleep(5)
from selenium.webdriver.common.by import By          # - 정보 획득
from selenium.webdriver.common.keys import Keys
# 로그인 하기
for i in range(665,len(attraction_name_list)+1):
    search_btn = browser.find_element(by=By.CSS_SELECTOR,value='#inp_search_mo')
    search_btn.click()
    text_input= browser.find_element(by=By.CSS_SELECTOR,value='#inp_search_index')
    try :
        delete_btn = browser.find_element(by=By.CSS_SELECTOR,value='body > div.search_index > div > div > div > div.form > button')
        delete_btn.click()
    except:
        pass
    text_input.send_keys(attraction_name_list[i])
    search_complete_btn = browser.find_element(by=By.CSS_SELECTOR,value='body > div.search_index > div > div > div > button.btn_search')
    search_complete_btn.click()
    time.sleep(5)
    attraction_title=''
    attraction_content = ''
    attraction_link = ''
    attraction_img=''
    try:
        big_box = browser.find_element(by=By.CSS_SELECTOR,value='#contents > div > div.box_leftType1 > div.proper_name.proper_on > div.cont')
        attraction_title = big_box.find_element(by=By.CSS_SELECTOR,value='div.properTitle > strong').text
        link_click =big_box.find_element(by=By.CSS_SELECTOR,value='#properTitle')
        link_click.click()
    except:
        try:
            attraction_title= browser.find_element(by=By.CSS_SELECTOR,value='#s_attraction > div.search_info_list > ul > li > div.cont > div.tit > a').text
            link_click = browser.find_element(by=By.CSS_SELECTOR,value='#s_attraction > div.search_info_list > ul > li > div.cont > div.tit > a')
            link_click.click()

        except:
            pass
    time.sleep(5)
    try:
        attraction_content = browser.find_element(by=By.CSS_SELECTOR,value='#topCp > div > h3').text
        attraction_img= browser.find_element(by=By.CSS_SELECTOR,value='#pImgList > div.swiper-slide.swiper-slide-active > img').get_attribute('src')
        attraction_link = browser.current_url
    except:
        pass
    print(attraction_title)
    print(attraction_link)
    print(attraction_content)
    print(attraction_img)
    attraction_search_info_collection.update_many({"attraction_name" :attraction_name_list[i]},{"$set" : {"attraction_title":attraction_title,"attraction_img":attraction_img,"attraction_link":attraction_link,'attraction_content':attraction_content}},upsert= True)


browser.quit()                                      # - 브라우저 종료
