from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('click on the first product')
def click_on_first_product(context):
    context.app.off_plan.click_on_product()

