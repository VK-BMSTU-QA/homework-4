import os
from selenium.webdriver import DesiredCapabilities, Remote
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from setup.auth import setup_auth


def default_setup(t):
    t.EMAIL = str.strip(os.environ['LOGIN'])
    t.PASSWORD = str.strip(os.environ['PASSWORD'])
    t.ROOT = str.strip(os.environ['ROOT'])

    browser = os.environ.get('BROWSER', 'CHROME')
    if t.driver is None:
        if browser == "CHROME":
            op = webdriver.ChromeOptions()
            # op.add_argument('headless')
            t.driver = webdriver.Chrome(service=Service(executable_path="./chromedriver"), options=op)
        else:
            t.driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    setup_auth(t)
