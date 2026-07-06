from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_livetv_playing(driver):
    # Step 1: Open homepage
    driver.get("https://www.indiatv.in/")

    # Step 2: Click Live TV link from homepage
    livetv_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.livetv"))
    )
    livetv_link.click()

    # Step 3: Switch into the Live TV iframe
    iframe = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )
    driver.switch_to.frame(iframe)

    # Step 4: Wait for video element to appear
    video = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "content_video_html5_api"))
    )

    # Step 5: Assert video is visible
    assert video.is_displayed(), "Live TV video player is not visible"

    # Step 6: Give it a moment for autoplay, then check it's playing
    time.sleep(3)
    is_paused = driver.execute_script(
        "return document.getElementById('content_video_html5_api').paused"
    )
    assert is_paused == False, "Live TV is not playing (it's paused)"

    # Step 7: Switch back to main page
    driver.switch_to.default_content()