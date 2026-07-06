import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    # This code runs BEFORE each test
    service = Service(executable_path="chromedriver.exe")
    drv = webdriver.Chrome(service=service)
    drv.maximize_window()

    yield drv   # <-- this hands the browser over to the test

    # This code runs AFTER each test (cleanup)
    drv.quit()