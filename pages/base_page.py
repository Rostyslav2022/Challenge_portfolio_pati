import os
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def field_send_keys(self, selector, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        return self.driver.find_element(selector_type, selector).click()

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    # def element_text(self):
    #     os.chmod(DRIVER_PATH, 755)
    #     self.driver_service = Service(executable_path=DRIVER_PATH)
    #     # self.driver.service = Service(executable.path = ChromeDriverManager().install())
    #     self.driver = webdriver.Chrome(service=self.driver_service)
    #     self.driver.get('https://scouts-test.futbolkolektyw.pl')
    #     self.driver.fullscreen_window()
    #     self.driver.implicitly_wait(IMPLICITLY_WAIT)
    #
    # def assert_element_text(self):
    #     actual_text = self.get_element_text('//*[@id="__next"]/form/div/div[1]/h5')
    #     expected_text = 'Scouts Panel'
    #     assert actual_text == expected_text
    #
    # def get_element_text(self, url):
    #     self.driver.get(url)
    #     return self.driver.title

    def assert_element_text(self):
        self.driver = 'https://scouts-test.futbolkolektyw.pl'
        self.xpath = '//*[@id="__next"]/form/div/div[1]/h5'
        self.expected_text = 'Scouts Panel'
        element = self.driver.find_element(by=By.XPATH, value=self.xpath)
        element = element.text
        element_text = element.text
        assert self.expected_text == element_text


