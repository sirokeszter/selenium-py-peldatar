# A program töltse be a példatárból az http://localhost:9999/scrolltoload.html oldalt. Mentsd le az első 20 macskás képet az oldalról.
# A fájlokat egy külön cats könyvtárba mentsd le. A fájlneve legyen a következő {sorszam}_{cat_id} ahol a sorszám alatt azt értjük,
# hogy hanyadiknak lett megjelenítve és cat_id meg az azonosító amit szolgáltató ad.
# A {} jelek ne legyenek benne a fájlnévben. (ez a feladat majdnem ugyan az, mint az előző feladat, csakhogy nincs load more gomb.)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import requests
import urllib.request

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("http://localhost:9999/scrolltoload.html")
    html = driver.find_element_by_tag_name("html")
    images = driver.find_elements_by_class_name("image")

    for i in range(2):
        time.sleep(3)
        html.send_keys(Keys.END)
    images = driver.find_elements_by_xpath("//div[@class='image']")
    images_url=[]
    for index,j in enumerate(images[0:21]):
        url = j.find_element_by_tag_name("img").get_attribute("scr")
        pict_name = j.find_element_by_tag_name("p").text.replace("Cat id:","")
        cat_file_name = f"{index}_{pict_name}"
        images_url.append(cat_file_name)
        print(images_url)

        reponse = requests.get(url)
        if reponse.status_code == 200:
            with open(f"cats/{cat_file_name}", "wb") as file:
                file.write(reponse.content)

        # r = requests.get(url)
        # if r.status_code == 200:
        #     with open(cat_file_name, 'wb') as f:
        #         f.write(r.content)
    print()


finally:
    driver.close()

