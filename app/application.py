from webbrowser import Chrome


from pages.base_page import Page
from pages.header import Header
from pages.main_page import MainPage
from pages.off_plan import OffPlan
from pages.sign_in_page import SignInPage


class Application:

    def __init__(self, driver):
        self.base_page= Page(driver)
        self.main_page = MainPage(driver)
        self.off_plan= OffPlan(driver)
        self.sign_in_page = SignInPage(driver)
        self.header= Header(driver)

