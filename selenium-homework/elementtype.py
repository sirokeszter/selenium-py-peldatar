from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#options=Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install())
try:
    elem1 = driver.find_element_by_id("element1")
    elem2 = driver.find_element_by_id("element2")
    elem3 = driver.find_element_by_id("element3")
    elem4 = driver.find_element_by_id("element4")
    elem5 = driver.find_element_by_id("element5")

    button = driver.find_element_by_xpath('//button')
    button.click()

    if elem1 == button:
        print(button.text)
        if elem2 == button:
            print(button.text)
            if elem3 == button:
                print(button.text)
                if elem4 == button:
                    print(button.text)
                    if elem5 == button:
                        print(button.text)

    result = driver.find_element_by_id("result")
    print(result.text)

    assert(result.text==f"{button.text} was clicked")

finally:
    driver.close()