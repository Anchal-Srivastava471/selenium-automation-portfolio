import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_signin(driver):
    # Step 1: Open login page
    driver.get("https://www.ampleimages.com/login")
    time.sleep(2)

    # Step 2: Fill Email
    # send_keys() = types text into the input field
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    email_field.send_keys("anchalsrivastava@indiatvnews.com")  # replace with real credentials

    # Step 3: Fill Password
    # By.NAME uses the name="" attribute from the HTML
    driver.find_element(By.NAME, "password").send_keys("Anchal@324")  # replace    , In step 2 & 3 we can use same method to fill fields but Wait (WebDriverWait) for the first element of a page/form to confirm it's loaded. After that, find_element is fine for the rest.

    # Step 4: Click Sign In button
    # CSS_SELECTOR targets elements using class names with a dot prefix
    driver.find_element(By.CSS_SELECTOR, "button.submit.btn").click()

    # Step 5: Verify login success
    # After login, URL usually changes OR a dashboard/profile element appears
    WebDriverWait(driver, 10).until(
        lambda d: d.current_url != "https://www.ampleimages.com/login"
    )
    assert "login" not in driver.current_url, "Login failed — still on login page"