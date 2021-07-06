# Lokátorral keresd ki az összes linket az oldalról.
# Tárold a memóriában egy listában az összes linket. A list tartalmát írd ki egy fájlba. Minden link egy új sorba kerüljön.
# A kimenetre írd ki hány linket találtál

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
from lxml import html
import requests

try:
    driver.get("http://localhost:9999")
    links = driver.find_elements_by_xpath('//body//table//a')
    current_url = driver.current_url
    list_of_links = []
    for i in range(len(links)):
        list_of_links.append(links[i].get_attribute('href'))

    for j in range(len(list_of_links)):
        print(list_of_links[j])

finally:
    driver.close()
