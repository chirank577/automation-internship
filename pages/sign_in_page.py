from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
from pages.base_page import Page



class SignInPage(Page):
    email_id=(By.ID, 'email-2')
    Password=(By.ID, 'field')
    continue_btn=(By.CSS_SELECTOR, "a[wized='loginButton']")

    def Login_page(self, user_id, password):
        self.input_text(user_id, *self.email_id)
        self.input_text(password, *self.Password)
        self.click(*self.continue_btn)


    def read_login_credentials(self):
        df = pd.read_excel('chiru.xlsx')
        print(df)

