from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get("http://localhost:9999/general.html")

try:
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        print(elem.get_attribute("href"))

finally:
    driver.close()
