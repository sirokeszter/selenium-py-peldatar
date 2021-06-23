from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get("http://localhost:9999/general.html")

try:
    links = []
    linkek = driver.find_elements_by_xpath("//*[@href]")

    for elem in linkek:  #
        url = elem.get_attribute('href')
        print(url)
        links.append(url)

    for i in linkek:
        assert (elem.text)

finally:
    driver.close()
