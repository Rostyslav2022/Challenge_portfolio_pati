from pages.base_page import BasePage


class Dashboard(BasePage):
   main_page_icon_xpath = "//*[contains(@class," MuiSvgIcon-root jss23 jss24")]"
   main_page_button_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]"
   main_page_xpath = "//*[contains(@class, "MuiTypography-root MuiListItemText")]"
   scouts_panel_description_xpath = "//*[contains(@class, "MuiTypography-body2")]"
   scouts_panel_block_xpath = "//*[contains(@class, "MuiCardContent - root")]"
   scouts_panel_xpath = "//*[contains(@class, "MuiTypography-root MuiTypography")]"
   scouts_panel_header_xpath = "//*[@id="__next"]/div[1]/header/div/h6"
   dev_team_contact_hyperlink_xpath = "// a[contains(@ href, '://')]"
   logo_scouts_panel_xpath = "//*[contains(@class, "MuiCardMedia")]"
   add_player_hyperlink_xpath = "//*[2][name()="a"]"
   super_man_hyperlink_xpath = "//h6//following-sibling::a[1]"
pass