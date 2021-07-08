# A program töltse be a példatárból a http://localhost:9999/pagination.html oldalt.
# Mentsd le az összes kontaktot az oldalról akinek a keresztneve (First Name) A betüvel kezdődik.
# A kiválasztott kontaktok összes adatát mentsd le memóriába egy szotár (dict) struktúrába. Amikor megvagy az összes adatot mentsd ki egy CSV file-ba.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import pprint
import csv

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("http://localhost:9999/pagination.html")
    extracted_data = []

    while True:
        time.sleep(2)
        table = driver.find_element_by_xpath("//table[@id='contacts-table']/tbody")
        rows = table.find_elements_by_tag_name("tr")
        for row in rows:
            data_row = {}
            cells = row.find_elements_by_tag_name("td")
            data_row["id"] = cells[0].text
            data_row["first_name"] = cells[1].text
            data_row["second_name"] = cells[2].text
            data_row["surname"] = cells[3].text
            data_row["second_surname"] = cells[4].text
            data_row["birth_data"] = cells[5].text
            if cells[1].text.startswith('A'):
                extracted_data.append(data_row)
        next_button = driver.find_element_by_id("next")
        if not next_button.is_enabled():
            break
        else:
            next_button.click()
        pprint.pprint(extracted_data)
        print(len(extracted_data))

    with open('ed.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(extracted_data)

finally:
    driver.close()
