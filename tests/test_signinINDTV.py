from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_signin_flow(driver):
    # Step 1: Open the homepage
    driver.get("https://www.indiatv.in/")
     # Step 2: Find the Sign In link using its title attribute
    # We use XPATH here because the link has a reliable title="Sign in"
    signin_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='Sign in']"))
    )
     # Step 3: Verify Sign In link is visible on homepage
    assert signin_link.is_displayed(), "Sign In link is not visible on homepage"
    # Step 4: Click the Sign In link
    signin_link.click()

    # Step 5: Verify we landed on the correct login page
    # driver.current_url gives us the current page URL as a string
    WebDriverWait(driver, 10).until(
        EC.url_contains("cms/login")
    )
    assert "cms/login" in driver.current_url, "Did not navigate to login page"
     # Step 6: Verify SKIP button is present on login page
    # We use CSS_SELECTOR: "button.skip_btn" means <button> with class skip_btn
    skip_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.skip_btn"))
    )
    assert skip_button.is_displayed(), "SKIP button is not visible on login page"
      # Step 7: Click SKIP and verify we go back to homepage
    skip_button.click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("indiatv.in")
    )
    assert "indiatv.in" in driver.current_url, "SKIP did not navigate back correctly"