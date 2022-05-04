import os
import unittest

import selenium
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from tests import Page, Component, Topbar
from tests.login_test import LoginPage


class PlaylistsPage(Page):
    PATH = 'playlist/289'

    @property
    def playlist_image(self):
        return PlaylistImage(self.driver)
    
    @property
    def topbar(self):
        return Topbar(self.driver)

    @property
    def text_block(self):
        return PlaylistTextBlock(self.driver)

    @property
    def edit_window(self):
        return PlaylistEditWindow(self.driver)


class PlaylistImage(Component):
    IMAGE = '//div[@class="playlist__description-avatar"]'

    def open_edit_window(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "playlist__description-avatar"))
        )
        self.driver.find_element_by_xpath(self.IMAGE).click()


class PlaylistTextBlock(Component):
    TITLE = '//div[@class="playlist__description-title"]'
    EDIT_WINDOW_BTN = '//div[@class="playlist__description-text playlist__description-edit-btn"]'

    def open_edit_window(self):
        btn = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDIT_WINDOW_BTN)
        )
        btn.click()

    def title(self):
        title = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TITLE).text
        )
        return title


class PlaylistEditWindow(Component):
    EDIT_WINDOW = '//div[@class="editwindow"]'
    CLOSE_BTN = '//img[@class="editwindow__close"]'
    TITLE_INPUT = '//input[@class="editwindow__form-input"]'
    SAVE_BUTTON = '//input[@class="editwindow__form-submit"]'
    DELETE_BUTTON = '//img[@class="editwindow__delete"]'
    WARNING_CLS = 'editwindow__form-msg'
    LINK = '//div[@class="editwindow__link"]'
    PUBLICITY_SWITCH = '//span[@class="slider"]'

    def is_open(self):
        try:
            window = WebDriverWait(self.driver, 10, 0.1).until(
                lambda d: d.find_element_by_xpath(self.EDIT_WINDOW)
            )
        except selenium.common.exceptions.TimeoutException:
            return False
        style = window.get_attribute("style")
        return "display: block;" in style

    def close_by_close_btn(self):
        button = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CLOSE_BTN)
        )
        button.click()

    def close_by_ext_area(self):
        area = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDIT_WINDOW)
        )
        area.click()

    def clear_title(self):
        input = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TITLE_INPUT)
        )
        input.clear()

    def set_title(self, title):
        input = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TITLE_INPUT)
        )
        input.clear()
        input.send_keys(title)

    def save(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "editwindow__form-submit"))
        )
        self.driver.find_element_by_xpath(self.SAVE_BUTTON).click()

    def fail_warning(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.text_to_be_present_in_element_attribute((By.CLASS_NAME, self.WARNING_CLS), "class", "fail")
        )
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.text_to_be_present_in_element_attribute((By.CLASS_NAME, self.WARNING_CLS), "class", "visible")
        )

    def click_on_delete(self):
        button = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DELETE_BUTTON)
        )
        button.click()

    def toggle_publicity(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.PUBLICITY_SWITCH))
        )
        self.driver.find_element_by_xpath(self.PUBLICITY_SWITCH).click()

    def success_warning(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.text_to_be_present_in_element_attribute((By.CLASS_NAME, self.WARNING_CLS), "class", "success")
        )
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.text_to_be_present_in_element_attribute((By.CLASS_NAME, self.WARNING_CLS), "class", "visible")
        )

    def playlist_link(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.text_to_be_present_in_element_attribute((By.XPATH, self.LINK), "style", "visibility: visible;")
        )


class PlaylistsTest(unittest.TestCase):
    EMAIL = os.environ['TESTUSERNAME']
    PASSWORD = os.environ['TESTPASSWORD']
    INVALID_TITLE = "dalwhdfpqjedlqwjedlwejflaiuwehf;efj;oWJDALEFNAKLWEHFLAEWHF"
    VALID_TITLE = "test Playlist"
    SETUP_TITLE = "playlist test"

    def setUp(self):
        browser = os.environ.get('TESTBROWSER', 'CHROME')
        options = Options()
        options.headless = bool(os.environ.get('HEADLESS', False))
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
            options=options
        )
        self.login_page = LoginPage(self.driver)
        self.login_page.open()
        self.login_form = self.login_page.form
        self.login_form.set_email(self.EMAIL)
        self.login_form.set_password(self.PASSWORD)
        self.login_form.login()
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.presence_of_element_located((By.CLASS_NAME, "avatar__img"))
        )

        self.playlists_page = PlaylistsPage(self.driver)
        self.playlists_page.open()

        WebDriverWait(self.driver, 10, 0.1).until(
            EC.presence_of_element_located((By.CLASS_NAME, "playlist__description-title"))
        )

    def tearDown(self):
        self.driver.quit()

    def test_edit_window_unauthorized(self):
        self.playlists_page.topbar.log_out()
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.element_attribute_to_include((By.ID, "signin-button"), "href")
        )
        self.playlists_page.playlist_image.open_edit_window()
        assert not self.playlists_page.edit_window.is_open()

    def test_edit_window(self):
        self.playlists_page.playlist_image.open_edit_window()
        assert self.playlists_page.edit_window.is_open()
        self.playlists_page.edit_window.close_by_close_btn()

        self.playlists_page.text_block.open_edit_window()
        assert self.playlists_page.edit_window.is_open()
        self.playlists_page.edit_window.close_by_ext_area()

    def test_submit_empty_form(self):
        self.playlists_page.text_block.open_edit_window()
        self.playlists_page.edit_window.clear_title()
        self.playlists_page.edit_window.save()
        self.playlists_page.edit_window.fail_warning()

    def test_submit_long_title(self):
        self.playlists_page.text_block.open_edit_window()
        self.playlists_page.edit_window.set_title(self.INVALID_TITLE)
        self.playlists_page.edit_window.save()
        self.playlists_page.edit_window.fail_warning()

    def test_submit_short_title(self):
        self.playlists_page.text_block.open_edit_window()
        self.playlists_page.edit_window.set_title(self.INVALID_TITLE[0:2])
        self.playlists_page.edit_window.save()
        self.playlists_page.edit_window.fail_warning()

    def test_confirm_deletion(self):
        self.playlists_page.text_block.open_edit_window()
        self.playlists_page.edit_window.click_on_delete()
        self.playlists_page.edit_window.fail_warning()

    def test_toggle_publicity(self):
        self.playlists_page.text_block.open_edit_window()
        self.playlists_page.edit_window.toggle_publicity()
        self.playlists_page.edit_window.success_warning()

        self.playlists_page.edit_window.toggle_publicity()
        self.playlists_page.edit_window.success_warning()
        self.playlists_page.edit_window.playlist_link()

    def test_positive_submit(self):
        self.playlists_page.text_block.open_edit_window()
        self.playlists_page.edit_window.set_title(self.VALID_TITLE)
        self.playlists_page.edit_window.save()
        self.playlists_page.edit_window.success_warning()
        self.playlists_page.edit_window.close_by_close_btn()
        assert self.playlists_page.text_block.title() == self.VALID_TITLE

        self.playlists_page.text_block.open_edit_window()
        self.playlists_page.edit_window.set_title(self.SETUP_TITLE)
        self.playlists_page.edit_window.save()
        self.playlists_page.edit_window.success_warning()
