import time
from time import sleep

from selenium.webdriver.common.by import By


from pages.base_page import Page


class OffPlan(Page):
    product=(By.XPATH,"//div[contains(text(), 'Vitalia Palm Jumeirah Residences')]")
    mobile_view_prooperty_detail=(By.CSS_SELECTOR,"a[wized='cardOfProperty']")
    new_product=(By.CSS_SELECTOR,"a[wized='cardOfProperty']")
    visualisations=(By.CSS_SELECTOR,"a.tab.w-inline-block.w-tab-link")
    # visualisations_text = (By.XPATH, "//a[@class='tab w-inline-block w-tab-link w--current'] //div")
    visualisations_text = (By.CSS_SELECTOR, 'a[class="tab w-inline-block w-tab-link w--current"]')


    def click_on_product(self):
        sleep(10)
        self.wait_to_be_clickable_click(*self.mobile_view_prooperty_detail)

        sleep(4)

    def verify_visualisations_three_options(self):
        expected=["Architecture", "Interior", "Lobby"]
        sleep(5)
        actual=[]
        self.driver.execute_script("window.scrollBy(0,100)", "")
        options=self.driver.find_elements(*self.visualisations)
        for option in options:
            option.click()
            sleep(10)

            # selected_option=self.driver.find_element(*self.visualisations_text).text
            selected_option = option.text
            print(selected_option)

            actual.append(selected_option)
        assert expected == actual,f' Expected{expected} but got Actual{actual}'







