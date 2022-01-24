import sys

from selenium.webdriver.common.by import By
from Src.PageObject.locators import Locator

sys.path.append(sys.path[0] + "/....")


class Main(object):
    def __init__(self, driver):
        self.driver = driver
        self.create_account = driver.find_element(By.XPATH, Locator.create_account)

    def create_account(self):
        return self.create_account
