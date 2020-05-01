from selenium import webdriver
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure

from Entripy.firstpage import Homepage
from Entripy.beforefirst import LoginPage


class TestLogin:
    @pytest.fixture(scope='class')
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:\\Users\\Tripath\\Desktop\\drivers\\chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        print("test completed")

    def test_login(self, test_setup):
        driver.get("https://www.entripy.com/")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/span[1]/div[3]/div[1]/a[2]"))).click()

        login = LoginPage(driver)
        login.enter_email('tripathpalsingh04@gmail.com')
        login.enter_password('h1rda45ingh')
        login.click_login()

    def test_homepage(self, test_setup):
        homepage = Homepage(driver)
        homepage.click_jackets()
        homepage.scroll()
        driver.save_screenshot("C:\\Users\\Tripath\\PycharmProjects\\untitled\\Entripy\\screenshot\\shot.png")
        #homepage.north()


