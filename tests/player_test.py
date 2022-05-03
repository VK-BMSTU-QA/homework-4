# -*- coding: utf-8 -*-

import os
import time
import unittest
from cProfile import label

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from sympy import O, sec

from tests.common import Albums, Page, Player, Sidebar, Topbar, Tracks, has_element
from tests.login_test import Component, LoginPage
from tests.main_test import MainPage
from tests.profile_test import ProfilePage

class PlayerTest(unittest.TestCase):
    EMAIL = os.environ['TESTUSERNAME']
    PASSWORD = os.environ['TESTPASSWORD']

    def setUp(self):
        browser = os.environ.get('TESTBROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        login_page = LoginPage(self.driver)
        login_page.open()

        login_form = login_page.form
        login_form.set_email(self.EMAIL)
        login_form.set_password(self.PASSWORD)
        login_form.login()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'avatar__img'))
        )

    def tearDown(self):
        self.driver.quit()

    def test_next_track(self):
        main_page = MainPage(self.driver)
        player = main_page.player
        tracks = main_page.tracks
        second_track = tracks.get_track_id(1)
        tracks.play_track()
        player.next_track()
        playing_track = player.get_playing_track_id()
        self.assertEqual(second_track, playing_track)

    def test_player_hidden(self):
        main_page = MainPage(self.driver)
        player = main_page.player
        self.assertTrue(player.hidden())

    def test_mute(self):
        main_page = MainPage(self.driver)
        player = main_page.player
        tracks = main_page.tracks
        tracks.play_track()
        player.mute()
        self.assertTrue(player.muted())

    def test_unmute(self):
        main_page = MainPage(self.driver)
        player = main_page.player
        tracks = main_page.tracks
        tracks.play_track()
        player.mute()
        player.mute()
        self.assertFalse(player.muted())
        
    def test_prev_disabled(self):
        main_page = MainPage(self.driver)
        player = main_page.player
        tracks = main_page.tracks
        tracks.play_track()
        self.assertTrue(player.prev_disabled())

    def test_next_enabled(self):
        main_page = MainPage(self.driver)
        player = main_page.player
        tracks = main_page.tracks
        tracks.play_track()
        self.assertFalse(player.next_disabled())

    def test_next_disabled(self):
        main_page = MainPage(self.driver)
        player = main_page.player
        tracks = main_page.tracks
        tracks.play_track(last=True)
        self.assertTrue(player.next_disabled())

    def test_prev_enabled(self):
        main_page = MainPage(self.driver)
        player = main_page.player
        tracks = main_page.tracks
        tracks.play_track(last=True)
        self.assertFalse(player.prev_disabled())