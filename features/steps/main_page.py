from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@given("open main reelly page")
def open_reelly_main_page(context):
    context.app.main_page.open_main()

@when('log in to the page using valid {user_id} and {password}')
def log_in_to_main_page(context, user_id, password):
    context.app.sign_in_page.Login_page(user_id=user_id, password=password)



@then('Verify the three options of visualization are available and clickable')
def verify_options_are_available(context):
    context.app.off_plan.verify_visualisations_three_options()


# @then('Verify the visualization options are clickable')
# def verify_options_are_clickable(context):
