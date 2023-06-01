from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from time import sleep

city_name = input()
# TODO: use title format for the city name and make sure it has "County" at the end if needed
if city_name != 'all':
    city_name = city_name.title()

driverPath = "chromedriver.exe"
s = Service(executable_path=driverPath)

browser = webdriver.Chrome(service=s)   
browser.get('https://www.cwb.gov.tw/V8/E/W/County/County.html?CID=63')  

tag1 = browser.find_element(By.XPATH, '//select[@id="CID"]')
# options = tag1.find_elements(By.XPATH, './option')

# try using the Select class
cities = Select(tag1)

if city_name == 'all':
    for option in cities.options:
        if option.is_enabled():
            cities.select_by_visible_text(f'{option.text}')
        else:
            continue

        temperature = browser.find_element(By.XPATH, '//*[@id="PC_Week_MOD"]/tbody/tr[1]/td[1]/p/span[@class="tem-C is-active"]').text
        
        print(f"{option.text}")
        print(f"{temperature}")
        
else:
    browser.find_element(By.XPATH, '//*[@id="CID"]').click()
    cities.select_by_visible_text(f'{city_name}')
    temperature = browser.find_element(By.XPATH, '//*[@id="PC_Week_MOD"]/tbody/tr[1]/td[1]/p/span[@class="tem-C is-active"]').text
    print(f"{city_name}")
    print(f"{temperature}")

browser.quit()
