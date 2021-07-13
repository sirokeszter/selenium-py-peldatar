# A program töltse be a példatárból a http://localhost:9999/editable-table.html oldalt. A megjelenő táblázatban az alábbi feladatokat kell végrehajtanod:
# a) Adj hozzá még két teljesen kitöltött sort. Ellenőrizd, hogy tényleg hozzáadódtak-e a sorok.
# b) Ellenőrizd a kereső funkciót.
# c) írd át a táblázat egyes celláit és ellenőrizd, hogy megfelelően frissült-e a DOM struktúra.

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
    driver.get("http://localhost:9999/editable-table.html")
    add_button= driver.find_element_by_tag_name("button")

    data_lists = [
        ("football", "49.50", 16, "Sporting goods"),
        ("basketball", "50.90", 8, "Sporting goods")
    ]

    # Sorok fejléc szerinti függvénye:
    def new_row(row, name, price, quantity, category):
        row.find_element_by_name('name').clear()
        row.find_element_by_name('name').send_keys(name)
        row.find_element_by_name('price').clear()
        row.find_element_by_name('price').send_keys(price)
        row.find_element_by_name('qty').clear()
        row.find_element_by_name('qty').send_keys(quantity)
        row.find_element_by_name('category').clear()
        row.find_element_by_name('category').send_keys(category)

   # Új sor megjelenítése:
    def new_rows_list(class_name):
        return driver.find_elements_by_class_name(class_name)

    # Két új sor hozzáadása:
    def add_rows(number_of_rows, data_lists):
        for i in range(number_of_rows):
            add_button.click()
            rows_list = new_rows_list('eachRow')
            new_row(rows_list[len(rows_list) - 1], *data_lists[i])

    print(add_rows(2, data_lists))

finally:
    pass
    # driver.close()