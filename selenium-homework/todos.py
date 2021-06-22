from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get("http://localhost:9999/todo.html")

try:
    todos = driver.find_elements_by_css_selector("span.done-false")

    for elt in todos:
        print(elt.text)

finally:
    driver.close()