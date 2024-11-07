from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@when('click on off plan at the left side menu')
def click_on_off_plan_option(context):
    context.app.header.click_off_plan_option()
