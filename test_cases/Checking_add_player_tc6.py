import os
import time
import unittest
from selenium import webdriver
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.add_player_page import AddPlayer
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestDashboardPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.name = "Zinedin"
        self.surname = "Zidan"

    def test_add_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_add_player()
        add_player = AddPlayer(self.driver)
        add_player.type_name(self.name)
        add_player.type_surname(self.surname)
        add_player.select_age("23/06/1972")
        add_player.select_leg("right")
        add_player.type_main_position("Midfielder")
        add_player.click_on_the_submit_button()
        time.sleep(5)


    @classmethod
    def tearDown(self):
        self.driver.quit()

