from selenium import webdriver


def test_demo():
    driver = webdriver.Chrome(executable_path="C:\\Users\\gayathri.nuthana\\Desktop\\Webdrivers\\chromedriver.exe")
    driver.implicitly_wait(2)
    driver.get("https://demoqa.com/automation-practice-form")
    assert driver.title == "DEMOQA"
    driver.maximize_window()
    driver.quit()

def test_google():
    driver = webdriver.Chrome(executable_path="C:\\Users\\gayathri.nuthana\\Desktop\\Webdrivers\\chromedriver.exe")
    driver.implicitly_wait(2)
    driver.get("https://www.google.com")
    assert driver.title == "Google"
    driver.maximize_window()
    driver.quit()
