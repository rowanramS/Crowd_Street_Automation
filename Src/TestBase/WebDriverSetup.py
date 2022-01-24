import unittest
from selenium import webdriver
import os
from pathlib import Path

from selenium.webdriver.chrome.options import Options


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        folder_path = str(Path(__file__).parents[0])

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_driver_path = os.path.join(folder_path, 'chromedriver')

        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        #self.driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)

        self.driver.implicitly_wait(3)
        self.driver.set_page_load_timeout(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
