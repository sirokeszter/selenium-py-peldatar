from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get("http://localhost:9999/general.html")

try:
    def get_all_links(driver):
        links = []
        elements = driver.find_elements_by_tag_name('a')
        for elem in elements:
            href = elem.get_attribute("href")
            links.append(href)
        return links

finally:
    driver.close()
