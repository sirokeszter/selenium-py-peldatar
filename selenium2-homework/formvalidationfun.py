# A program töltse be a példatárból az http://localhost:9999/simplevalidation.html oldalt.
# A tanultak alapján teszteld le az űrlap mező ellenőrző funkcióit.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("http://localhost:9999/simplevalidation.html")
    button = driver.find_element_by_id("test-button").click()

    inputs = ["test-email",
                            "test-password",
                            "test-confirm-password",
                            "test-customer-number",
                            "test-dealer-number",
                            "test-random-field",
                            # csak placeholder="Optional, but if exists should contain the word "twelve""
                            "test-date-field",
                            "test-url-field",  # ???? placeholder="Optionally enter a URL"
                            "test-random-textarea",
                            "test-card-type",
                            "test-card-number",
                            "test-card-cvv",
                            "test-card-month",
                            "test-card-year",
                            "single-checkbox-invalid",
                            "test-save-email-yes",
                            "test-terms-service",
                            "test-terms-service-more"]

    error_msg_texts = ["Please enter an e-mail",
                            "This field can't be empty",
                            "Please complete Desired Password",
                            "This field can't be empty",
                            "This field can't be empty",
                            "This field can't be empty",
                            # csak placeholder="Optional, but if exists should contain the word "twelve""
                            "This field can't be empty",
                            "This field can't be empty",  # ???? placeholder="Optionally enter a URL"
                            "This field can't be empty",
                            "Please select a card type",
                            "Please enter a credit card number (no spaces)",
                            "Please enter a credit card number (no spaces)",
                            "Select a month",
                            "Select a year",
                            "This field can't be empty",
                            "test-save-email-yes",
                            "Please agree to both to continue",
                            "Please agree to both to continue"]

    error_messages = driver.find_elements_by_class_name("validate-field-error-message")

    for i in range(len(inputs)):
        inputs = driver.find_element_by_id(f"{inputs[i]}").send_keys("")
        for j in error_messages:
            msg_text = j.text
            assert msg_text == error_msg_texts[i]

        # msg = WebDriverWait(driver, 20).until(
        #     EC.visibility_of_element_located((By.ID, "f{id}"))).get_attribute(
        #     "validationMessage")
        # assert msg is not None
        # assert msg == "Please agree to both to continue"
        # time.sleep(1)

finally:
    driver.close()
