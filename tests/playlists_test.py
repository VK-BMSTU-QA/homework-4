import os
import unittest

from Login.LoginPage import LoginPage
from Playlist.PlaylistPage import PlaylistPage
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.chrome.options import Options


class PlaylistsTest(unittest.TestCase):
    EMAIL = os.environ["TESTUSERNAME"]
    PASSWORD = os.environ["TESTPASSWORD"]
    INVALID_TITLE = "dalwhdfpqjedlqwjedlwejflaiuwehf;efj;oWJDALEFNAKLWEHFLAEWHF"
    VALID_TITLE = "test Playlist"
    SETUP_TITLE = "playlist test"

    def setUp(self):
        browser = os.environ.get("TESTBROWSER", "CHROME")
        options = Options()
        options.headless = True
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
