from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get("http://localhost:9999/trickyelements.html")

try:
    element1 = driver.find_element_by_id("element1")
    element2 = driver.find_element_by_id("element2")
    element3 = driver.find_element_by_id("element3")
    element4 = driver.find_element_by_id("element4")
    element5 = driver.find_element_by_id("element5")

    elements = ["element1", "element2", "element3", "element4", "element5"]

    for e in elements:
        e_elements = driver.find_element_by_id(e)
        button = driver.find_element_by_xpath('//button')
        result = driver.find_element_by_id("result")
        if e_elements == button:
            button.click()
            print(result.text)
            assert (result.text == f"{button.text} was clicked")

finally:
    driver.close()
