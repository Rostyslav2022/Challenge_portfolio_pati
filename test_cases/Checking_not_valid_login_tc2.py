import os
import time
import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage (unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        #self.driver.service = Service(executable.path = ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)


    def test_not_valid_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('...')
        user_login.click_on_the_sign_in_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()