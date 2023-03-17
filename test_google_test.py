import time

from selenium import webdriver

driver=None
def setup_module(module):
    global driver
    driver = webdriver.Chrome(executable_path="C:\\Users\\gayathri.nuthana\\Desktop\\Webdrivers\\chromedriver.exe")
    driver.implicitly_wait(2)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")

def teardown_module(module):
    driver.quit()

def test_google_title():
    assert driver.title == 'Google'

def test_title():
    driver.get("https://demoqa.com/text-box")
    time.sleep(3)
    assert driver.title == 'DEMOQA'