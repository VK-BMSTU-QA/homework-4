import os
import unittest

from Login.LoginPage import LoginPage
from Playlist.PlaylistComponents import PlaylistEditWindow
from Playlist.PlaylistPage import PlaylistPage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests.utils import CHECK_FREQ, TIMEOUT


class PlaylistsTest(unittest.TestCase):
    EMAIL = os.environ["TESTUSERNAME"]
    PASSWORD = os.environ["TESTPASSWORD"]
    INVALID_TITLE = "dalwhdfpqjedlqwjedlwejflaiuwehf;efj;oWJDALEFNAKLWEHFLAEWHF"
    VALID_TITLE = "test Playlist"
    SETUP_TITLE = "playlist test"

    def setUp(self):
        browser = os.environ.get("TESTBROWSER", "CHROME")
        options = Options()
        options.headless = bool(os.environ.get("HEADLESS", False))
        self.driver = Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
            options=options
        )
        self.login_page = LoginPage(self.driver)
        self.login_page.login(self.EMAIL, self.PASSWORD)

        self.playlists_page = PlaylistPage(self.driver)
        self.playlists_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_edit_window_unauthorized(self):
        self.playlists_page.topbar.log_out()
        self.playlists_page.playlist_image.open_edit_window()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
                lambda d: PlaylistEditWindow.IS_OPEN not in d.find_element(by=By.XPATH, value=PlaylistEditWindow.EDIT_WINDOW).get_attribute('style')
        ))
            

    def test_edit_window(self):
        self.playlists_page.playlist_image.open_edit_window()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
                lambda d: PlaylistEditWindow.IS_OPEN in d.find_element(by=By.XPATH, value=PlaylistEditWindow.EDIT_WINDOW).get_attribute('style')
            ))
        self.playlists_page.edit_window.close_by_close_btn()

        self.playlists_page.text_block.open_edit_window()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
                lambda d: PlaylistEditWindow.IS_OPEN in d.find_element(by=By.XPATH, value=PlaylistEditWindow.EDIT_WINDOW).get_attribute('style')
            ))
        self.playlists_page.edit_window.close_by_ext_area()

    def test_submit_empty_form(self):
        self.playlists_page.text_block.open_edit_window()
        self.playlists_page.edit_window.clear_title()
        self.playlists_page.edit_window.save()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
                EC.text_to_be_present_in_element_attribute((By.CLASS_NAME, PlaylistEditWindow.WARNING_CLS), "class", "fail visible")
            ))

    def test_submit_long_title(self):
        self.playlists_page.text_block.open_edit_window()
        self.playlists_page.edit_window.set_title(self.INVALID_TITLE)
        self.playlists_page.edit_window.save()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
                EC.text_to_be_present_in_element_attribute((By.CLASS_NAME, PlaylistEditWindow.WARNING_CLS), "class", "fail visible")
            ))

    def test_submit_short_title(self):
        self.playlists_page.text_block.open_edit_window()
        self.playlists_page.edit_window.set_title(self.INVALID_TITLE[0:2])
        self.playlists_page.edit_window.save()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
                EC.text_to_be_present_in_element_attribute((By.CLASS_NAME, PlaylistEditWindow.WARNING_CLS), "class", "fail visible")
            ))

    def test_confirm_deletion(self):
        self.playlists_page.text_block.open_edit_window()
        self.playlists_page.edit_window.click_on_delete()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
                EC.text_to_be_present_in_element_attribute((By.CLASS_NAME, PlaylistEditWindow.WARNING_CLS), "class", "fail visible")
            ))

    def test_toggle_publicity(self):
        self.playlists_page.text_block.open_edit_window()
        self.playlists_page.edit_window.toggle_publicity()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
                EC.text_to_be_present_in_element_attribute((By.CLASS_NAME, PlaylistEditWindow.WARNING_CLS), "class", "success visible")
            ))

        self.playlists_page.edit_window.toggle_publicity()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
                EC.text_to_be_present_in_element_attribute((By.CLASS_NAME, PlaylistEditWindow.WARNING_CLS), "class", "success visible")
            ))
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
                EC.text_to_be_present_in_element_attribute((By.XPATH, PlaylistEditWindow.LINK), "style", "visibility: visible;")
        ))

    def test_positive_submit(self):
        self.playlists_page.text_block.open_edit_window()
        self.playlists_page.edit_window.set_title(self.VALID_TITLE)
        self.playlists_page.edit_window.save()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
                EC.text_to_be_present_in_element_attribute((By.CLASS_NAME, PlaylistEditWindow.WARNING_CLS), "class", "success visible")
            ))
        self.playlists_page.edit_window.close_by_close_btn()
        self.assertEqual(self.playlists_page.text_block.title(), self.VALID_TITLE)

        self.playlists_page.text_block.open_edit_window()
        self.playlists_page.edit_window.set_title(self.SETUP_TITLE)
        self.playlists_page.edit_window.save()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
                EC.text_to_be_present_in_element_attribute((By.CLASS_NAME, PlaylistEditWindow.WARNING_CLS), "class", "success visible")
            ))
