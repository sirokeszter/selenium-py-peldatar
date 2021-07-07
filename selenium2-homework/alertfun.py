# A program töltse be a példatárból a http://localhost:9999/alert_playground.html oldalt.
# A tanultak alapján az összes alert funkcióra írj selenium kódot.
# A prompt-nál teszteld le a be, hogy a beírt érték megjelenik-e egy paragraf tagben, miután eltűnt az alert.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("http://localhost:9999/alert_playground.html")
    # Alert button:
    alert_button = driver.find_element_by_name("alert")
    alert_button.click()
    ref_text1 = "I am alert"
    alert1 = driver.switch_to.alert
    assert (alert1.text == ref_text1)
    print(alert1.text)
    time.sleep(2)
    alert1.accept()  # megnézzük,miután megnyomtuk, eltűnik-e
    time.sleep(1)

    # Confirmation button:
    conf_button = driver.find_element_by_name("confirmation")
    conf_button.click()
    ref_text2 = "I am confirm"
    alert2 = driver.switch_to.alert
    assert (alert2.text == ref_text2)
    print(alert2.text)
    time.sleep(2)
    alert2.accept()  # megnézzük,miután megnyomtuk, eltűnik-e
    time.sleep(1)

    # Prompt button:
    prompt_button = driver.find_element_by_name("prompt")
    prompt_button.click()
    ref_text3 = "I am prompt"
    alert3 = driver.switch_to.alert
    assert (alert3.text == ref_text3)
    print(alert3.text)
    time.sleep(2)
    alert3.accept()  # megnézzük,miután megnyomtuk, eltűnik-e
    time.sleep(1)

    # Double-click button:
    dc_button= driver.find_element_by_id("double-click")
    actionChains = ActionChains(driver)
    actionChains.double_click(dc_button).perform()
    ref_text4 = "You double clicked me!!!, You got to be kidding me"
    alert4 = driver.switch_to.alert
    assert (alert4.text == ref_text4)
    print(alert4.text)
    time.sleep(2)
    alert4.accept() #megnézzük,miután megnyomtuk, eltűnik-e
    time.sleep(1)

finally:
    driver.close()