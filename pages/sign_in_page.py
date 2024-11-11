from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page
from sample_script import driver


class SignInPage(Page):
    email_id=(By.ID, 'email-2')
    Password=(By.ID, 'field')
    continue_btn=(By.CSS_SELECTOR, "a[wized='loginButton']")

    def Login_page(self, user_id, password):
        self.input_text(user_id, *self.email_id)
        self.input_text(password, *self.Password)
        self.click(*self.continue_btn)

