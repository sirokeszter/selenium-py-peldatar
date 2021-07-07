# A program töltse be a példatárból az http://localhost:9999/forms.html oldalt. Koncentrálj a dátum mezőkre.
# A célod, hogy ezeket a dátum és idő értékeket selenium segítségével automatikusan beállítsd.

from datetime import datetime, date, time, timezone
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from tkcalendar import DateEntry

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("http://localhost:9999/forms.html")

date1 = driver.find_element_by_id("example-input-date").send_keys("002021-06-05")
date2 = driver.find_element_by_id("example-input-date-time").send_keys("2021.05.05 05:05:05:555")
date3 = driver.find_element_by_id("example-input-date-time-local").send_keys("002000-05-12-12-01")
date4 = driver.find_element_by_id("example-input-month").send_keys("1995\tdecember")
date5 = driver.find_element_by_id("example-input-week").send_keys("52.hét,2015")
date6 = driver.find_element_by_id("example-input-time").send_keys("12:15")