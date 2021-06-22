from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get("http://localhost:9999/kitchensink.html")

try:
    bmwradio = driver.find_element_by_id("bmwradio")
    print(bmwradio.text)
    benzradio = driver.find_element_by_id("benzradio")
    print(benzradio.text)
    hondaradio = driver.find_element_by_id("hondaradio")
    print(hondaradio.text)

    mse = driver.find_element_by_name("multiple-select-example")
    print(mse.text)

    openwindow = driver.find_element_by_xpath('//*[@id="openwindow"]')
    print(openwindow.text)

finally:
    driver.close()
