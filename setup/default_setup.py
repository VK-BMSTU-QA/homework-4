import os
from selenium.webdriver import DesiredCapabilities, Remote

from setup.auth import setup_auth


def default_setup(t):
    """ Осуществляет авторизацию в account.mail.ru и настраивает браузер.
    :param t: unittest.TestCase
    :return: None
    """
    t.EMAIL = os.environ['LOGIN']
    t.PASSWORD = os.environ['PASSWORD']

    browser = os.environ.get('BROWSER', 'CHROME')

    t.driver = Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=getattr(DesiredCapabilities, browser).copy()
    )

    setup_auth(t)
