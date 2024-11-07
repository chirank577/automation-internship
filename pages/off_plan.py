from time import sleep

from selenium.webdriver.common.by import By


from pages.base_page import Page


class OffPlan(Page):
    product=(By.XPATH,"//div[contains(text(), 'Mackerel Tower')]")
    visualisations=(By.CSS_SELECTOR,"a.tab.w-inline-block.w-tab-link")
    visualisations_text = (By.XPATH, "//a[@class='tab w-inline-block w-tab-link w--current'] //div")

    def click_on_product(self):
        self.wait_to_be_clickable_click(*self.product)

    def verify_visualisations_three_options(self):
        expected=["Architecture", "Interior", "Lobby"]

        actual=[]
        options=self.driver.find_elements(*self.visualisations)
        for option in options:
            option.click()
            sleep(4)

            selected_option=option.find_element(*self.visualisations_text).text
            print(selected_option)

            actual.append(selected_option)
        assert expected == actual,f' Expected{expected} but got Actual{actual}'







