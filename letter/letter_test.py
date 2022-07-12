import unittest
import os

from selenium import webdriver

from letter.page import LetterPage
from utils.utils import Utils
import utils.constants as constants

from time import sleep

class Letter(unittest.TestCase):
    def setUp(self):
        BROWSER = os.environ.get("BROWSER")
        if BROWSER not in constants.browsers_list.keys():
            raise ValueError("Wrong browser set")

        self.driver = webdriver.Remote(command_executor="http://localhost:4444",
                                       options=constants.browsers_list[BROWSER])

        # self.driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver')

        self.driver.implicitly_wait(10)

        self.utils = Utils(driver=self.driver)
        self.letterPage = LetterPage(self.driver)
        self.utils.login()
        self.letterPage.read_all()

    def test_default_letter(self):
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_header()
        self.letterPage.fill_letter()
        self.letterPage.send_letter()
        self.letterPage.close_sent_popup()
        # self.driver.refresh()
        while not self.letterPage.get_new_letters_status():
            print('Something happened with website, trying to check again...')
        topic, letter = self.letterPage.get_letter_by_inbox()
        self.assertEqual(topic.text, 'SAMPLE TEXT')
        self.assertEqual(letter.text, 'SAMPLETEXT SAMPLETEXT SAMPLETEXT SAMPLETEXT\n  ')
        topic, letter = self.letterPage.get_letter_by_sent()
        self.assertEqual(topic.text, 'Self: SAMPLE TEXT')
        self.assertEqual(letter.text, 'SAMPLETEXT SAMPLETEXT SAMPLETEXT SAMPLETEXT\n  ')

    def test_send_letter_with_no_receiver(self):
        self.letterPage.click_on_new_letter_button()
        self.letterPage.send_letter()
        error = self.letterPage.get_no_receiver_error()
        self.assertEqual(error.text, 'Не указан адрес получателя')

    def test_send_letter_without_topic(self):
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_receiver()
        self.letterPage.fill_letter()
        self.letterPage.send_letter()
        self.letterPage.close_sent_popup()
        # self.driver.refresh()
        while not self.letterPage.get_new_letters_status():
            print('Something happened with website, trying to check again...')
        topic, letter = self.letterPage.get_letter_by_inbox()
        self.assertEqual(topic.text, '<Без темы>')
        self.assertEqual(letter.text, 'SAMPLETEXT SAMPLETEXT SAMPLETEXT SAMPLETEXT\n  ')
        topic, letter = self.letterPage.get_letter_by_sent()
        self.assertEqual(topic.text, 'Self:')
        self.assertEqual(letter.text, 'SAMPLETEXT SAMPLETEXT SAMPLETEXT SAMPLETEXT\n  ')

    def test_send_empty_letter(self):
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_receiver()
        self.letterPage.send_letter()
        self.letterPage.confirm_empty_letter()
        self.letterPage.close_sent_popup()
        # self.driver.refresh()
        while not self.letterPage.get_new_letters_status():
            print('Something happened with website, trying to check again...')
        topic, letter = self.letterPage.get_letter_by_inbox()
        self.assertEqual(topic.text, '<Без темы>')
        self.assertEqual(letter.text, '   ')

    def test_cancel_letter(self):
        ex_topic, ex_letter = self.letterPage.get_letter_by_inbox()
        ex_topic, ex_letter = ex_topic.text, ex_letter.text
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_header()
        self.letterPage.fill_letter()
        self.letterPage.cancel_letter()
        topic, letter = self.letterPage.get_letter_by_inbox()
        self.assertEqual(topic.text, ex_topic)
        self.assertEqual(letter.text, ex_letter)

    def test_add_to_templates(self):
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_header()
        self.letterPage.fill_letter()
        self.letterPage.add_to_templates()
        self.letterPage.cancel_letter()
        topic, letter = self.letterPage.get_template()
        self.assertEqual(topic.get_attribute('value'), 'SAMPLE TEXT')
        self.assertEqual(letter.text, 'SAMPLETEXT SAMPLETEXT SAMPLETEXT SAMPLETEXT\n\nБЕЗ ПОДПИСИ')

    def test_resize_new_letter_popup(self):
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_header()
        self.letterPage.fill_letter()
        ex_topic, ex_letter = self.letterPage.get_letter()
        ex_topic, ex_letter = ex_topic.get_attribute('value'), ex_letter.text

        topic, letter = self.letterPage.resize_letter_popup()
        self.assertEqual(topic.get_attribute('value'), ex_topic)
        self.assertEqual(letter.text, ex_letter)

        topic, letter = self.letterPage.resize_letter_popup()
        self.assertEqual(topic.get_attribute('value'), ex_topic)
        self.assertEqual(letter.text, ex_letter)

    def test_close_letter(self):
        ex_topic, ex_letter = self.letterPage.get_letter_by_inbox()
        ex_topic, ex_letter = ex_topic.text, ex_letter.text
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_header()
        self.letterPage.fill_letter()
        self.letterPage.close_letter()
        topic, letter = self.letterPage.get_letter_by_inbox()
        self.assertEqual(topic.text, ex_topic)
        self.assertEqual(letter.text, ex_letter)

    def test_collapse_then_expand_letter(self):
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_header()
        self.letterPage.fill_letter()
        ex_topic, ex_letter = self.letterPage.get_letter()
        ex_topic, ex_letter = ex_topic.get_attribute('value'), ex_letter.text
        self.letterPage.collapse_letter()
        self.letterPage.expand_letter()
        topic, letter = self.letterPage.get_letter()
        self.assertEqual(topic.get_attribute('value'), ex_topic)
        self.assertEqual(letter.text, ex_letter)

    def test_collapse_then_check_draft(self):
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_header()
        self.letterPage.fill_letter()
        ex_topic, ex_letter = self.letterPage.get_letter()
        ex_topic, ex_letter = ex_topic.get_attribute('value'), ex_letter.text
        self.letterPage.collapse_letter()
        topic, letter = self.letterPage.get_draft()
        self.assertEqual(topic.get_attribute('value'), ex_topic)
        self.assertEqual(letter.text, ex_letter)

    def test_offer_call(self):
        self.letterPage.click_on_new_letter_button()
        letter = self.letterPage.offer_call()
        self.assertEqual(letter.text.split(': ')[0], 'Перейдите по ссылке, чтобы подключиться к звонку')

    def test_important_letter(self):
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_header()
        self.letterPage.fill_letter()
        self.letterPage.toggle_importance()
        self.letterPage.send_letter()
        self.letterPage.close_sent_popup()
        while not self.letterPage.get_new_letters_status():
            print('Something happened with website, trying to check again...')
        importance_badge = self.letterPage.get_importance_status()
        self.assertEqual(len(importance_badge), 1)

    def test_notification_letter(self):
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_header()
        self.letterPage.fill_letter()
        self.letterPage.toggle_notification()
        self.letterPage.send_letter()
        self.letterPage.close_sent_popup()
        while not self.letterPage.get_new_letters_status():
            print('Something happened with website, trying to check again...')
        self.letterPage.mark_letter_as_read()
        while not self.letterPage.get_new_letters_status():
            print('Something happened with website, trying to check again...')
        notification_topic = self.letterPage.get_read_status()
        self.assertEqual(notification_topic.text, 'Подтверждение прочтения')

    def test_translate_letter(self):
        text_for_translation = 'тест'
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_header()
        translated_text = self.letterPage.translate_letter(text_for_translation)
        self.assertEqual(translated_text, 'test')

    def test_cancel_translation(self):
        text_for_translation = 'тест'
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_header()
        not_translated_text = self.letterPage.cancel_translation(text_for_translation)
        self.assertEqual(not_translated_text, 'тест')

    def test_insert_signature(self):
        self.letterPage.click_on_new_letter_button()
        _, ex_letter = self.letterPage.get_letter()
        ex_letter = ex_letter.text

        self.letterPage.clear_format()
        _, cleared_letter = self.letterPage.get_letter()
        cleared_letter = cleared_letter.text
        self.assertNotEqual(cleared_letter, ex_letter)

        self.letterPage.insert_signature()
        _, signed_letter = self.letterPage.get_letter()
        self.assertNotEqual(signed_letter.text, cleared_letter)
        self.assertEqual(signed_letter.text, ex_letter)

    def tearDown(self):
        self.driver.quit()
