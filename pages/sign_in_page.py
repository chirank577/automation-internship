from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import openpyxl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        # df = pd.read_excel('chiru.xlsx')
        # print(df)

        # for index, row in df.iterrows():
        #     username = row['username']
        #     password = row['password']
        #
        #     print(username)
        #     print(password)
        #
        #     self.input_text(username, *self.email_id)
        #     self.input_text(password, *self.Password)
        #     self.click(*self.continue_btn)
        #
        #     try:
        #         # Check if login was successful (example: looking for a logout button)
        #         success_element = self.find_element(By.XPATH,"//h1[text()='Total projects']")
        #         print(f"Test Passed for {username}")
        #     except:
        #         print(f"Test Failed for {username}")
        #
        #         # Add delay between iterations for demo purposes
        #     sleep(2)
        # quit()


        # Load the Excel file
        df = pd.read_excel('chiru.xlsx')  # Replace with your file path
        print("Loaded Data:")
        print(df)

        # Add a Result column if it doesn't exist
        if "Result" not in df.columns:
            df["Result"] = ""
            df["Result"] = df["Result"].astype(str)

        for index, row in df.iterrows():
            username = row['username']
            password = row['password']

            # Input username
            email_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.email_id)
            )
            email_field.clear()
            email_field.send_keys(username)

            # Input password
            password_field = self.driver.find_element(*self.Password)
            password_field.clear()
            password_field.send_keys(password)

            # Click the login button
            self.click(*self.continue_btn)
            sleep(10)

            # Check if login was successful
            success_element_present = self.driver.find_element(By.CSS_SELECTOR,"a.menu-text-link-leaderboard.w--current")
            if success_element_present.text == "Off-plan":
                sleep(5)


            # Update the result column
                print(f"Login Passed for: {username}")
                df.at[index, "Result"] = "Passed"
            else:
                print(f"Login Failed for: {username}")
                df.at[index, "Result"] = "Failed"

            # Optional delay
            sleep(2)

        # Save the updated results back to an Excel file
        updated_file = 'updated_chiru.xlsx'
        df.to_excel(updated_file, index=False)
        print(f"Results saved to {updated_file}")



