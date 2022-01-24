import random
import string
import sys
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

sys.path.append(sys.path[0] + "/...")

from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.create_account import CreateAccount
import unittest


class AccountCreation(WebDriverSetup):

    def test_Account_Page(self):
        driver = self.driver
        driver.get("https://test.crowdstreet.com./invexp/accounts/create-account/")

        account_page = CreateAccount(driver)

        account_page.first_name_input.send_keys("Bob")
        account_page.last_name_input.send_keys("Doe")

        email = ''.join(random.choice(string.ascii_letters) for x in range(10)) + "@gmail.com"
        account_page.email_input.send_keys(email)

        account_page.password_input.send_keys("Password1!")
        account_page.confirm_password_input.send_keys("Password1!")

        account_page.accredited_yes_radio.click()

        account_page.tos_checkbox.click()

        WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it(account_page.captcha_iframe))

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

        driver.switch_to.default_content()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(account_page.submit_button)).click()

        # time.sleep(50)

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='head-link']")))

        self.assertTrue("Sign Out" in driver.page_source, "Account has been created")


if __name__ == '__main__':
    unittest.main()
