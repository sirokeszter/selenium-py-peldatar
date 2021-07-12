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
    num_guess = driver.find_element_by_id("numberOfGuesses").text

    buttons = []
    for button in range(100):
        buttons.append(driver.find_element_by_id(button))

    main_window = driver.window_handles[0]
    i = 0
    x = False
    while not x:
        buttons[i].click()
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
        color = driver.find_element_by_tag_name("h1").text
        x = (color == target_color or i >=99)
        num = driver.find_element_by_tag_name("h1").text
        driver.close()
        driver.switch_to.window(main_window)
        i += 1
    print("Matched color:", color)

finally:
    pass
# driver.close()
