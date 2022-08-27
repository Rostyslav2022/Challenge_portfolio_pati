import os
import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestCheckButtonText(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_check_text(self):
        actual_title = self.get_page_text('https://scouts-test.futbolkolektyw.pl/en')
        expected_title = 'Scouts panel - sign in'
        assert actual_title == expected_title

    def get_page_text(self, url):
        self.driver.get(url)
        return self.driver.title

    @classmethod
    def tearDown(self):
        self.driver.quit()



