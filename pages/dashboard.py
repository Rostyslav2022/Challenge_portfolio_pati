import time
from pages.base_page import BasePage
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


class Dashboard(BasePage):
      main_page_icon_xpath = "//*[contains(@class,' MuiSvgIcon-root jss23 jss24')]"
      main_page_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]"
      main_page_xpath = "//*[contains(@class, 'MuiTypography-root MuiListItemText')]"
      scouts_panel_description_xpath = "//*[contains(@class, 'MuiTypography-body2')]"
      scouts_panel_block_xpath = "//*[contains(@class, 'MuiCardContent - root')]"
      scouts_panel_xpath = "//*[contains(@class, 'MuiTypography-root MuiTypography)]"
      scouts_panel_header_xpath = "//*[@id='__next']/div[1]/header/div/h6"
      dev_team_contact_hyperlink_xpath = "// a[contains(@ href, '://')]"
      logo_scouts_panel_xpath = "//*[contains(@class, 'MuiCardMedia')]"
      add_player_hyperlink_xpath = "//*[2][name()='a']"
      super_man_hyperlink_xpath = "//h6//following-sibling::a[1]"
      players_count_element_xpath ='// *[ @ id = "__next"] / div[1] / main / div[2] / div[1] / div / div[1]'
      # expected_title = 'Scouts Panel'
      # dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'

      expected_title = 'Scouts panel'
      dashboard_url = 'https://scouts-test.futbolkolektyw.pl'
      element_text = 'Scouts Panel'
      element_text_xpath = '//*[@id="__next"]/form/div/div[1]/h5'


      def title_of_page(self):
          self.wait_for_element_to_be_clickable(self.logo_scouts_panel_xpath)
          assert self.get_page_title(self.dashboard_url) == self.expected_title

      def click_on_the_main_page_icon_xpath(self):
          self.click_on_the_element(self.main_page_icon_xpath)

      def visibility_of_element_located(self):
            self.click_on_the_element(self.players_count_element_xpath)


