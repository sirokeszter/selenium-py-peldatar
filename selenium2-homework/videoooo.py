# A program töltse be a példatárból az http://localhost:9999/videos.html oldalt.
# Az oldalon található összes beágyazott videót indítsa el és állítsa meg.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("http://localhost:9999/videos.html")
    html5videos=driver.find_element_by_id("html5video")
    html5videos.click()
    html5videos.send_keys(Keys.SPACE)
    time.sleep(6)
    js = "pause-video.js;"
    driver.execute_script(js)

    video1_playbtn = driver.find_element_by_xpath("/html/body/div/button[1]")
    video1_playbtn.click()
    time.sleep(3)
    video1_playbtn.click()
    #
    # #youtube_video=driver.find_element_by_id("player-container")
    # driver.get("https://www.youtube.com/embed/tgbNymZ7vqY")
    # WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
    #     (By.XPATH, "//button[@aria-label='Lejátszás']"))).click()
    # #button=driver.find_element_by_xpath("//button[@aria-label='Lejátszás']").send_keys(Keys.SPACE)

    frameElement = driver.find_element_by_xpath("//iframe[@src='https://www.youtube.com/embed/tgbNymZ7vqY']")
    driver.switch_to.frame(frameElement)
    driver.find_element_by_xpath("//button[@aria-label='Lejátszás']").click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath("//button[@aria-label='Lejátszás']").click()

finally:
    pass
    #driver.close()
