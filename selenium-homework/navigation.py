from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')


def navigate_to_general_page():
    link = driver.find_element_by_xpath('//a[text()="General text and other elements"]')
    link.click()


driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
try:
    driver.get("http://localhost:9999/")
    print(driver.current_url)
    navigate_to_general_page()
    print(driver.current_url)
    driver.back()
    print(driver.current_url)
    navigate_to_general_page()

    anchors = []
    links = driver.find_elements_by_xpath("//*[@href]")

    for elem in links:  #
        current_url = elem.get_attribute('href')
        print(current_url)
        anchors.append(current_url)

    print("-" * 30)

    while driver.current_url != "http://localhost:9999/":
        print(driver.current_url)
        driver.back()

finally:
    driver.close()
