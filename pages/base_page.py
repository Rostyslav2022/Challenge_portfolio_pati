import time
from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.settings import DEFAULT_LOCATOR_TYPE, EXPLICITLY_WAIT


class BasePage:

    def __init__(self, driver: WebDriver):
        self.add_player_hyperlink_xpath = "//*[2][name()='a']"
        self.players_count_element_xpath = '// *[ @ id = "__next"] / div[1] / main / div[2] / div[1] / div / div[1] '
        self.driver = driver

    def field_send_keys(self, selector, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        return self.driver.find_element(selector_type, selector).click()

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_element_text(self, driver, xpath, expected_text):
        """Comparing expected text with observed value from web element
            :param driver: webdriver instance
            :param xpath: xpath to element with text to be observed
            :param expected_text: text what we expecting to be found
            :return: None
        """
        element = driver.find_element(by=By.XPATH, value=xpath)
        element_text = element.text
        assert expected_text == element_text

    # def assert_element_text(self):
    #     self.driver = 'https://scouts-test.futbolkolektyw.pl'
    #     self.xpath = '//*[@id="__next"]/form/div/div[1]/h5'
    #     self.expected_text = 'Scouts Panel'
    #     element = self.driver.find_element(by=By.XPATH, value=self.xpath)
    #     element = element.text
    #     element_text = element.text
    #     assert self.expected_text==element_text

    def wait_for_element_to_be_clickable(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        time.sleep(10)

    def visibility_of_element_located(self):
        element = '// *[ @ id = "__next"] / div[1] / main / div[2] / div[1] / div / div[1] '
        WebDriverWait(self, driver, 10).until(EC.visibility_of(element))
        time.sleep(10)

    def print_nice_word(self):
        if self.players_count_element_xpath == '// *[ @ id = "__next"] / div[1] / main / div[2] / div[1] / div / div[1] ':
            print('Well done))))))))')
        else:
            print('Try another way')

    def click_on_add_player(self):
        self.click_on_the_element(self.add_player_hyperlink_xpath)
