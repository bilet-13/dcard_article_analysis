from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time 

opt = Options()
opt.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36')
# opt.add_argument('--cookie=dcsrd=CbQpI4WBmoVQxY0yEd2T3DS_; dcard-web-oauth-cv=UUpJcU82Q2JDNWVfbzZfTkRBUFNkd1VrOVpOcHJfZmZyZDY3VlNBVXZfYw==; \
#     dcard-web-oauth-cv.sig=JH3lrFutPuGGCZ3y86cc1KLWlFU; \
#         __cf_bm=hPlz3BQOhP9jrhDeWbNHKJYRihtS3PgNDXjwcfKJqKw-1650643134-0-AXgk691lu8XUp8WcfK1FjHLbTCQDmRfG19SnusjwzgnqaA0fIsSGtNkAxzCrQlYREBqP+MyhfopjD32zQFp4gx4=')

chrome = webdriver.Chrome('chromedriver.exe', options=opt)
print (chrome.execute_script('return navigator.userAgent'))

dict_forums = {
    'ntu' : 50, 'ncku' : 50, 'ntpu' : 20, 'nycu' : 10
    }

login_url = 'https://id.dcard.tw/oauth/login'
chrome.get(login_url)
tmp = input()# input everything after finsishing logining

for name, number in dict_forums.items():
    time.sleep(30)
    url = 'https://www.dcard.tw/service/api/v2/forums/' + name + '/posts' + '?limit=' + str(number)
    context = chrome.get(url)
    time.sleep(2)
    element = chrome.find_element(By.TAG_NAME, 'pre')
    time.sleep(2)
  

    fpath = name + time.strftime('%m-%d', time.localtime()) +'.txt'
    with open(fpath, 'w', encoding='UTF-8') as f:
        f.write(element.text)



