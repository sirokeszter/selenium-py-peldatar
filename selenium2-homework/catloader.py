# A program töltse be a példatárból az http://localhost:9999/loadmore.html oldalt.
# Mentsd le az első 20 macskás képet az oldalról. A fájlokat egy külön cats könyvtárba mentsd le.
# A fájlneve legyen a következő {sorszam}_{cat_id} ahol a sorszám alatt azt értjük, hogy hanyadiknak lett megjelenítve és cat_id meg az azonosító, amit szolgáltató ad.
# A {} jelek ne legyenek benne a fájlnévben.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import urllib.request

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("http://localhost:9999/loadmore.html")
    load_more = driver.find_element_by_xpath("//div[@class='load-more-button']/button")
    for i in range(4):
        time.sleep(3)
        images = driver.find_elements_by_xpath("//div[@class='image']")
        for j in images[:5]:
            url = j.find_element_by_tag_name("img").get_attribute("scr")
            pict_name = j.find_element_by_tag_name("p").text
            pname= pict_name.replace("Cat id:","")
            print(pname)
            #urllib.request.urlretrieve(url, f"{pname}.jpg")
        load_more.click()

finally:
    driver.close()
