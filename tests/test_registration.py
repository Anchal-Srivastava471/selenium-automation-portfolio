import time
#WHAT: Brings in Python's built-in time tool
# WHY: We need time.sleep() to pause script between actions
from selenium import webdriver
# WHAT: Brings in the main Selenium tool
# WHY: Selenium is what controls the browser
from selenium.webdriver.common.by import By
# WHAT: Brings in the "By" tool for finding elements
# WHY: Tells Selenium HOW to search — by NAME, ID, XPATH etc
from selenium.webdriver.support.ui import WebDriverWait
# WHAT: Brings in the smart waiting tool
# WHY: Makes script wait until something is ready (not just fixed seconds)
from selenium.webdriver.support import expected_conditions as EC
# WHAT: Brings in conditions like "is element clickable?" "is element visible?"
# WHY: WebDriverWait needs to know WHAT to wait for — EC defines that
from selenium.webdriver.support.ui import Select
# WHAT: Brings in special tool only for dropdown menus
# WHY: Normal find_element cannot handle <select> dropdowns

def test_registration(driver):

    # Step 1: Open login page
    driver.get("https://www.ampleimages.com/login")
    time.sleep(3)

    # Step 2: Click Register tab
    register_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li[text()='Register']"))
    )
     # WHAT: Waits up to 10 seconds for the Register tab to be clickable
    # WHY: Tab might not be ready immediately after page loads
     # NOTE: By.XPATH "//li[text()='Register']" means
    #       find any <li> tag whose text is exactly "Register"
    #       We use XPATH here because tab has no id or name — only text
    register_tab.click()
     # WHAT: Clicks the Register tab
    # WHY: Switches the form from Sign In to Register
    time.sleep(3)

    # Step 3: First Name
    fname = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "fname"))
    )
     # WHAT: Waits up to 10 seconds for First Name field to be clickable
    # WHY: This is the FIRST field — confirms entire register form is loaded
     # NOTE: By.NAME, "fname" matches <input name="fname"> in HTML
    driver.execute_script("arguments[0].scrollIntoView(true);", fname)
    # WHAT: Scrolls the page until First Name field is visible on screen
     # NOTE: arguments[0] always means "the element I passed in" — here fname
    fname.send_keys("Test")
     # WHAT: Types "Test" into the First Name field
    # WHY: Filling in the required form data

    # Step 4: Last Name
    lname = driver.find_element(By.NAME, "lname")
     # WHY: Form is already confirmed loaded in Step 3 so no wait needed
    driver.execute_script("arguments[0].scrollIntoView(true);", lname)
    lname.send_keys("User")

    # Step 5: Company Type dropdown
    ctype = driver.find_element(By.NAME, "ctype")
     # WHAT: Finds the Company Type dropdown element
    # WHY: We need to store it before wrapping with Select()
    driver.execute_script("arguments[0].scrollIntoView(true);", ctype)
     # WHAT: Scrolls to the dropdown
    # WHY: Must be visible before interacting
    Select(ctype).select_by_visible_text("Creative Agency")
    # WHAT: Opens dropdown and selects "Creative Agency" option
    # WHY: Normal click/send_keys can't pick options from <select> dropdowns
     # NOTE: select_by_visible_text picks by EXACTLY what you see on screen
    #       Other options: select_by_value("Creative Agency")
    #                      select_by_index(1) — picks by position

    # Step 6: Company Name
    cname = driver.find_element(By.NAME, "cname")
    driver.execute_script("arguments[0].scrollIntoView(true);", cname)
    cname.send_keys("Test Company")

    # Step 7: Job Title dropdown
    job = driver.find_element(By.NAME, "job_title")
    driver.execute_script("arguments[0].scrollIntoView(true);", job)
    Select(job).select_by_visible_text("Tester")

    # Step 8: Email unique every run
    email = f"testuser{int(time.time())}@example.com"
      # WHAT: Creates a unique email using current timestamp
    # WHY: Registration fails if email already exists in database
    cemail = driver.find_element(By.NAME, "cemail")
    driver.execute_script("arguments[0].scrollIntoView(true);", cemail)
    cemail.send_keys(email)
     # WHY: Required field — must be unique each run

    # Step 9: Mobile
    phone = driver.find_element(By.NAME, "telephone")
    driver.execute_script("arguments[0].scrollIntoView(true);", phone)
    phone.send_keys("9876543210")

    # Step 10: Password via JavaScript
    pwd = driver.find_element(By.NAME, "password")
    driver.execute_script("arguments[0].scrollIntoView(true);", pwd)
    time.sleep(1)
    driver.execute_script("arguments[0].value = 'Test@1234';", pwd)
    driver.execute_script("arguments[0].dispatchEvent(new Event('input'));", pwd)
    driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", pwd)

    # Step 10.5: Dismiss cookie popup if it appears
    # WHAT: Tries to find and click the ACCEPT button on cookie banner
    # WHY: Cookie popup overlays the page and blocks the submit button
    # THINK OF IT AS: Closing a popup before continuing
    try:
        cookie_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='ACCEPT']"))
        )
        cookie_btn.click()
        time.sleep(1)
        print("--- Cookie popup dismissed ---")
    except:
        print("--- No cookie popup found, continuing ---")
    # NOTE: We use try/except here because popup may or may not appear
    # If popup not found in 5 seconds — no crash, just moves on

    # Step 11: Submit
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button.submit.btn")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", submit_btn)

    # Step 12: Verify success
    time.sleep(3)
    print(f"\n--- URL after submit: {driver.current_url} ---")
    assert "login" not in driver.current_url, \
        f"Registration failed — still on: {driver.current_url}"