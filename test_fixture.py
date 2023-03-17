import time

import pytest
from selenium import webdriver

driver=None
@pytest.fixture(scope='module')
def init_driver():
    global driver
    driver = webdriver.Chrome(executable_path="C:\\Users\\gayathri.nuthana\\Desktop\\Webdrivers\\chromedriver.exe")
    driver.implicitly_wait(2)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")
    yield
    driver.quit()

def test_google_title(init_driver):
    assert driver.title == "Google"

def test_title(init_driver):
    driver.get("https://demoqa.com/text-box")
    # time.sleep(3)
    assert driver.title == 'DEMOQA'