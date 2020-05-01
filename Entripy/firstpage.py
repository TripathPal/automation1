from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Homepage:

    def __init__(self, driver):
        self.driver = driver

        self.jackets_link_xpath = "//*[@id='main']/span[1]/div[3]/div[3]/div[1]/div[4]/a"
        self.scroll_link_xpath = "//*[@id='main']/div[9]/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[7]/div"
        #self.north_xpath = "//*[@id='main']/div[9]/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[8]/div"

    def click_jackets(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.jackets_link_xpath))).click()

    def scroll(self):
        element = self.driver.find_element_by_xpath(self.scroll_link_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    #def north(self):
        #self.driver.find_element_by_xpath(self.north_xpath).click()


