import sys

from selenium.webdriver.common.by import By

from Src.PageObject.locators import Locator

sys.path.append(sys.path[0] + "/....")


class CreateAccount(object):
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = driver.find_element(By.XPATH, Locator.first_name_input)
        self.last_name_input = driver.find_element(By.XPATH, Locator.last_name_input)

        self.email_input = driver.find_element(By.XPATH, Locator.email_input)

        self.password_input = driver.find_element(By.XPATH, Locator.password_input)
        self.confirm_password_input = driver.find_element(By.XPATH, Locator.confirm_password_input)

        self.accredited_yes_radio = driver.find_element(By.XPATH, Locator.accredited_yes_radio)
        self.accredited_no_radio = driver.find_element(By.XPATH, Locator.accredited_no_radio)

        self.tos_checkbox = driver.find_element(By.XPATH, Locator.tos_checkbox)

        self.captcha_iframe = driver.find_element(By.CSS_SELECTOR, Locator.captcha_iframe)

        self.submit_button = driver.find_element(By.XPATH, Locator.submit_button)

    def first_name_input(self):
        return self.first_name_input

    def last_name_input(self):
        return self.last_name_input

    def password_input(self):
        return self.password_input

    def confirm_password_input(self):
        return self.confirm_password_input

    def accredited_yes_radio(self):
        return self.accredited_yes_radio

    def accredited_no_radio(self):
        return self.accredited_no_radio

    def tos_checkbox(self):
        return self.tos_checkbox

    def submit_button(self):
        return self.submit_button
