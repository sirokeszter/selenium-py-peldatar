# A program töltse be a példatárból az http://localhost:9999/windowgame.html oldalt.
# A feladatot, hogy megtaláld a random kiválasztott színhez tartozó gombot. Ha egy gombra rákattintasz az egy új ablakot fog feldobni, egy valamilyen színben tündököl.
# Ügyelj arra, hogy ne árassza el a képernyődet a sok ablak.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random


options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("http://localhost:9999/windowgame.html")
    target_color = driver.find_element_by_id("target_color").text
    buttons=driver.find_elements_by_tag_name("button")
    #option['+str(randomNumber)+']']").click()
    for button in buttons:
        button.click()
        main_window = driver.window_handles[0]
        driver.execute_script("window.open('','newwin','height=800,width=600')")
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
        colors = driver.find_elements_by_xpath("/html/body/h1")
        for i in colors:
            color=driver.find_element_by_tag_name("h1").text
            if color.text != target_color.text:
                new_window.quit()
                continue
            else:
                break

finally:
    pass
# driver.close()
