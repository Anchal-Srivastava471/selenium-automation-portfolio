import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_hamburger_icon(driver):
    # Step 1: Open the website
    driver.get("https://www.indiatv.in/")
    time.sleep(2)  # Allow JS-heavy sticky header to fully render

    # Step 2: Wait for hamburger icon to be clickable
    hamburger = WebDriverWait(driver, 20).until(  # increased from 10 to 20
        EC.element_to_be_clickable((By.ID, "openMenu"))
    )

    # Step 3: Assert it is visible
    assert hamburger.is_displayed(), "Hamburger icon is not visible on the page"

    # Step 4: Scroll into view, then JS click (avoids sticky header overlap issues)
    driver.execute_script("arguments[0].scrollIntoView(true);", hamburger)
    driver.execute_script("arguments[0].click();", hamburger)  # JS click

    # Step 5: Wait for menu to get the "on" class
    WebDriverWait(driver, 10).until(
        lambda d: "on" in d.find_element(By.ID, "menu").get_attribute("class")
    )

    # Step 6: Final confirmation
    menu_class = driver.find_element(By.ID, "menu").get_attribute("class")
    assert "on" in menu_class, "Menu did not open after clicking hamburger icon"