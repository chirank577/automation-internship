
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver

from app.application import Application
from support.logger import logger


# Command to run tests with Allure & Behave:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_search.feature

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    # """
    mobile_emulation = {"deviceName": "Nexus 5"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service, options=chrome_options)

     #firefox
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ### SAFARI ###
    # context.driver = webdriver.Safari()

    ### BROWSERS WITH DRIVERS: provide path to the driver file ###
    # service = Service(executable_path='put your path to driver file here')
    # context.driver = webdriver.Firefox(service=service)

    # HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'chiranjivikumar_Vu9JqR'
    # bs_key = 'WeGs1aHqsuZW7UUMjptN'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os" : "Windows",
    #     "osVersion" : "11",
    #     'browserName': 'chrome',
    #     'sessionName': scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait=WebDriverWait(context.driver, timeout=10)
    context.app=Application(context.driver)


def before_scenario(context, scenario):
    logger.info(f'\n Started scenario: {scenario.name}')
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Failed step: {step}')


def after_scenario(context, feature):
    context.driver.quit()
