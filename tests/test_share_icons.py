import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_share_icons(driver):

    # Step 1: Open page
    driver.get("https://www.indiatv.in/gallery/religion-vastu-shastra-me-batayi-gayi-3-baton-ka-bhumi-kharidte-samay-rakhain-dhyan-2026-06-24-1227188")
    time.sleep(3)
    

    # Step 2: Verify WhatsApp icon visible
    whatsapp = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a.whatsapp"))
    )
    assert whatsapp.is_displayed(), "WhatsApp icon not visible"
    
    # Step 3: Scroll to share area and force open popup
    share_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.shares.btn"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", share_btn)
    time.sleep(2)

    # Force open popup
    driver.execute_script("""
        document.querySelector('div.shares-opt').classList.add('on');
    """)
    time.sleep(2)

    # Step 4: Verify all icons visible
    facebook = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "span.facebook"))
    )
    assert facebook.is_displayed(), "Facebook not visible"

    twitter = driver.find_element(By.CSS_SELECTOR, "span.twitter")
    assert twitter.is_displayed(), "Twitter not visible"

    linkedin = driver.find_element(By.CSS_SELECTOR, "span.linkedin")
    assert linkedin.is_displayed(), "LinkedIn not visible"

    pinterest = driver.find_element(By.CSS_SELECTOR, "span.pinterest")
    assert pinterest.is_displayed(), "Pinterest not visible"

    # Step 5: Test FACEBOOK window
    original_window = driver.current_window_handle
    # WHAT: Saves original window before any clicks
    # WHY: We need to come back to this window after each social test

    driver.execute_script("arguments[0].click();", facebook)
    time.sleep(3)
    all_windows = driver.window_handles
    assert len(all_windows) > 1, "Facebook window did not open"

    # Switch to new window
    for window in all_windows:
        if window != original_window:
            driver.switch_to.window(window)
            break
    time.sleep(2)
    assert "facebook" in driver.current_url.lower(), "Not Facebook page"
    

    # Close and return to original
    driver.close()
    driver.switch_to.window(original_window)
    # WHAT: Close FB window and go back to article page
    # WHY: Must return to original before testing next icon
    # THINK OF IT AS: Closing one tab and going back to main tab
    time.sleep(2)

    # Step 6: Reopen popup and test TWITTER window

    # Popup closes after click — need to reopen it
    driver.execute_script("""
        document.querySelector('div.shares-opt').classList.add('on');
    """)
    # WHAT: Reopens the popup again
    # WHY: After clicking FB and returning, popup is closed
    #      We must reopen it before clicking next icon
    time.sleep(2)

    twitter = driver.find_element(By.CSS_SELECTOR, "span.twitter")
    driver.execute_script("arguments[0].click();", twitter)
    time.sleep(3)
    all_windows = driver.window_handles
    assert len(all_windows) > 1, "Twitter window did not open"

    for window in all_windows:
        if window != original_window:
            driver.switch_to.window(window)
            break
    time.sleep(2)

    assert "twitter" in driver.current_url.lower() or \
           "x.com" in driver.current_url.lower(), "Not Twitter page"
    # WHAT: Checks URL contains "twitter" OR "x.com"
    # WHY: Twitter rebranded to X so URL could be either
    

    driver.close()
    driver.switch_to.window(original_window)
    time.sleep(2)

    # Step 7: Reopen popup and test LINKEDIN window

    driver.execute_script("""
        document.querySelector('div.shares-opt').classList.add('on');
    """)
    time.sleep(2)

    linkedin = driver.find_element(By.CSS_SELECTOR, "span.linkedin")
    driver.execute_script("arguments[0].click();", linkedin)
    time.sleep(3)
    all_windows = driver.window_handles
    assert len(all_windows) > 1, "LinkedIn window did not open"

    for window in all_windows:
        if window != original_window:
            driver.switch_to.window(window)
            break
    time.sleep(2)
    
    assert "linkedin" in driver.current_url.lower(), "Not LinkedIn page"
    

    driver.close()
    driver.switch_to.window(original_window)
    time.sleep(2)

    # Step 8: Reopen popup and test PINTEREST window

    driver.execute_script("""
        document.querySelector('div.shares-opt').classList.add('on');
    """)
    time.sleep(2)

    pinterest = driver.find_element(By.CSS_SELECTOR, "span.pinterest")
    driver.execute_script("arguments[0].click();", pinterest)
    time.sleep(3)
    all_windows = driver.window_handles
    assert len(all_windows) > 1, "Pinterest window did not open"

    for window in all_windows:
        if window != original_window:
            driver.switch_to.window(window)
            break
    time.sleep(2)
    assert "pinterest" in driver.current_url.lower(), "Not Pinterest page"

    driver.close()
    driver.switch_to.window(original_window)
   