from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    elem1 = driver.find_element_by_id("element1")
    elem2 = driver.find_element_by_id("element2")
    elem3 = driver.find_element_by_id("element3")
    elem4 = driver.find_element_by_id("element4")
    elem5 = driver.find_element_by_id("element5")

    elemek= [elem1, elem2, elem3, elem4, elem5]
    button = driver.find_element_by_xpath('//button')

    for i in elemek:
        if elemek[i]==button:
            button.click()
            result = driver.find_element_by_id("result")
            print(result.text)
            break
            assert(result.text=="element{} was clicked".format(i))

finally:
    driver.close()