from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
#options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get("http://localhost:9999/trickyelements.html")

try:
    element1 = driver.find_element_by_id("element1")
    element2 = driver.find_element_by_id("element2")
    element3 = driver.find_element_by_id("element3")
    element4 = driver.find_element_by_id("element4")
    element5 = driver.find_element_by_id("element5")

    if element1 = driver.find_elements_by_xpath('//button'):


    for i in elements:
        if elements[i] == button:
            button.click()
            result = driver.find_element_by_id("result")
            print(result.text)
            break
            assert (result.text == "element{} was clicked".format(i))

finally:
    driver.close()
