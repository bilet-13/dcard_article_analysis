from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep
import time
import json


school_forms = ['ntu', 'ncku', 'ntpu', 'nycu']
dcard_url = 'https://www.dcard.tw/f/'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

required_num = int(input('請輸入想要爬取的資料個數'))

for school in school_forms:

    url = dcard_url + school
    driver.get(url)

    results = []

    while len(results) < required_num:
        sleep(5)
        try:
            elements = driver.find_elements(By.TAG_NAME, 'article')
        except:
            pass
       
        for element in elements:
            try:
                title = element.find_element(By.TAG_NAME, 'a').text
                print(title)
                href_element = element.find_element(By.TAG_NAME, 'h2')
                href = href_element.find_element(By.TAG_NAME, 'a').get_attribute('href')
                #print(href)
                # subtitle = element.find_element(By.CLASS_NAME, 'atm_d2_1gzgpud atm_ks_15vqwwr m15ojj43').text
                result = {
                    'title': title,
                    'href': href,
                    # 'subtitle': subtitle
                }
                if result not in results:
                    results.append(result)
                    print(result)

            except:
                print('error loop')
                pass

        js = "window.scrollTo({\
            top : document.body.scrollHeight,\
            left : 0,\
            behavior: 'smooth'\
            });"
        
        driver.execute_script(js)

    fpath = school + time.strftime('%m-%d', time.localtime()) + '-' + str(required_num) + '.json' 

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(results[ : required_num ], f, indent=2, ensure_ascii=False)

driver.quit()