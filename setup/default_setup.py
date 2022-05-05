import os
from selenium.webdriver import DesiredCapabilities, Remote
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from setup.auth import setup_auth


def default_setup(t):
    t.EMAIL = os.environ['LOGIN']
    t.PASSWORD = os.environ['PASSWORD']

    browser = os.environ.get('BROWSER', 'CHROME')
    if browser == "CHROME":
        t.driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
    else:
        t.driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    # t.driver = Remote(
    #     command_executor='http://127.0.0.1:4444/wd/hub',
    #     desired_capabilities=getattr(DesiredCapabilities, browser).copy()
    # )

    # setup_auth(t)
