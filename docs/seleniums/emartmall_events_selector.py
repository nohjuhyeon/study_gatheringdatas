# https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033&page=1
# https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033&page=2
# ...
# https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033&page=10

# * 웹 크롤링 동작
from selenium import webdriver 
import time

# ChromeDriver 실행
# Chrome WebDriver의 capabilities 속성 사용
# capabilities = browser.capabilities

browser = webdriver.Chrome()                        # - chrome browser 열기

pass
browser.get("")                                     # - 주소 입력

                                                    # - 가능 여부에 대한 OK 받음
pass
html = browser.page_source                          # - html 파일 받음(and 확인)

from selenium.webdriver.common.by import By          # - 정보 획득


browser.quit()                                      # - 브라우저 종료
