from page_objects.login import LoginPage


def setup_auth(test):
    auth_page = LoginPage(test.driver)
    auth_page.open()

    auth_page.login(test.EMAIL, test.PASSWORD)