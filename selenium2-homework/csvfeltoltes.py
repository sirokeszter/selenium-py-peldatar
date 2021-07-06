# A program töltse be a példatárból a http://localhost:9999/another_form.html oldalt.
# A program segítségével olvasd be a csv tartalmat. A feladatod, hogy az oldalon található formanyomtatvány segítségével feltöltsd a táblázatot.
# Használd a Python CSV könyvtárát. A feltöltött táblázatot ellenőrizheted ha a probramod letölti a táblázat alatti gomb segítségével az aktuális tartalmat.
# Hasonlítsd össze python kódból a kapott file-t, hogy identikus-e az eredetivel.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("http://localhost:9999/another_form.html")


    def find_and_clear_by_id(id):
        element = driver.find_element_by_id(id)
        element.clear()
        return element


    submit_button = driver.find_element_by_id("submit")

    with open('table_in.csv', encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
            print(row)
            find_and_clear_by_id("fullname").send_keys(row[0])
            find_and_clear_by_id("email").send_keys(row[1])
            find_and_clear_by_id("dob").send_keys(row[2])
            find_and_clear_by_id("phone").send_keys(row[3])
            submit_button.click()

    result_rows = driver.find_elements_by_xpath("//table[@id='detailsTable']/tbody/tr")

    for row in result_rows:
        cells = row.find_elements_by_tag_name("td")
        print(cells[0].text, cells[1].text, cells[2].text, cells[3].text)

    # A szöveg azonosság vizsgálata:
    assert()

finally:
    pass
    # driver.close()
