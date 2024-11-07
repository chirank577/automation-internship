
from selenium.webdriver.common.by import By

from pages.base_page import Page

class Header(Page):
    click_on_off_plan=(By.CSS_SELECTOR, "a._1-link-menu.w-inline-block.w--current")

    def click_off_plan_option(self):
        self.click(*self.click_on_off_plan)