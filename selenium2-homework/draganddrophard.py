# A program töltse be a példatárból az http://localhost:9999/dragndrop2.html oldalt.
# A feladatod, hogy a todo oszlobpól átrakd az összes kártyát a doing oszlopba.
# dnd.js

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from os import getcwd
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.maximize_window()

try:
    driver.get("http://localhost:9999/dragndrop2.html")
    time.sleep(1)

    cwd = getcwd()
    JS_DRAG_DROP = open(cwd + '\\dnd.js', 'r').read()
    print(JS_DRAG_DROP)
    # drag and drop is an element on another one
    source_ids=("Pizza","Tacos","BBQ","Burgers")
    for id in source_ids:
        source = driver.find_element_by_id(id)
        target = driver.find_element_by_id("Doing")

        driver.execute_script(JS_DRAG_DROP, source, target)

    driver.implicitly_wait(2)

finally:
    pass
