from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://eupalyazatiportal.hu/")

nemletezik=driver.find_element_by_id("nemletezik")
nemletezik.click()
