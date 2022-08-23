from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@id='__next']/form/div/div[2]/button/span[1]"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    expected_title = "Scouts panel - sign in"
    title_of_box_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    header_of_box = 'Scouts Panel'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        xpath = '//*[@id="__next"]/form/div/div[1]/h5'
        self.element_text = driver.find_element(by=By.XPATH, value=xpath)

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def field_send_keys (self, selector,value,locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def get_assert_element_text(self):
        assert self.element_text == self.expected_text('Scouts Panel')
