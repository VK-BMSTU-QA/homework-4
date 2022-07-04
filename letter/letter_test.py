import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from letter.page import LetterPage
from utils.utils import Utils

from time import sleep

class Letter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver')
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.utils = Utils(driver=self.driver)
        self.letterPage = LetterPage(self.driver)
        self.utils.login()
    
    def test_default_letter(self):
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_header()
        self.letterPage.fill_letter()
        self.letterPage.send_letter()
        self.driver.refresh()
        topic, letter = self.letterPage.check_letter_by_inbox()
        self.assertEqual(topic.text, 'SAMPLE TEXT')
        self.assertEqual(letter.text, 'SAMPLETEXT SAMPLETEXT SAMPLETEXT SAMPLETEXT\n  ')
        topic, letter = self.letterPage.check_letter_by_sent()
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
        self.driver.refresh()
        topic, letter = self.letterPage.check_letter_by_inbox()
        self.assertEqual(topic.text, '<Без темы>')
        self.assertEqual(letter.text, 'SAMPLETEXT SAMPLETEXT SAMPLETEXT SAMPLETEXT\n  ')
        topic, letter = self.letterPage.check_letter_by_sent()
        self.assertEqual(topic.text, 'Self:')
        self.assertEqual(letter.text, 'SAMPLETEXT SAMPLETEXT SAMPLETEXT SAMPLETEXT\n  ')
    
    def test_send_empty_letter(self):
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_receiver()
        self.letterPage.send_letter()
        self.letterPage.confirm_empty_letter()
        self.driver.refresh()
        topic, letter = self.letterPage.check_letter_by_inbox()
        self.assertEqual(topic.text, '<Без темы>')
        self.assertEqual(letter.text, '   ')
    
    def test_cancel_letter(self):
        ex_topic, ex_letter = self.letterPage.check_letter_by_inbox()
        ex_topic, ex_letter = ex_topic.text, ex_letter.text
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_header()
        self.letterPage.fill_letter()
        self.letterPage.cancel_letter()
        topic, letter = self.letterPage.check_letter_by_inbox()
        self.assertEqual(topic.text, ex_topic)
        self.assertEqual(letter.text, ex_letter)

    def test_add_to_templates(self):
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_header()
        self.letterPage.fill_letter()
        self.letterPage.add_to_templates()
        self.letterPage.cancel_letter()
        topic, letter = self.letterPage.check_template()
        self.assertEqual(topic.get_attribute('value'), 'SAMPLE TEXT')
        self.assertEqual(letter.text, 'SAMPLETEXT SAMPLETEXT SAMPLETEXT SAMPLETEXT\n\nБЕЗ ПОДПИСИ')

    def test_resize_new_letter_popup(self):
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_header()
        self.letterPage.fill_letter()
        ex_topic, ex_letter = self.letterPage.get_letter()
        ex_topic, ex_letter = ex_topic.get_attribute('value'), ex_letter.text

        topic, letter = self.letterPage.check_resize()
        self.assertEqual(topic.get_attribute('value'), ex_topic)
        self.assertEqual(letter.text, ex_letter)

        topic, letter = self.letterPage.check_resize()
        self.assertEqual(topic.get_attribute('value'), ex_topic)
        self.assertEqual(letter.text, ex_letter)
    
    def test_close_letter(self):
        ex_topic, ex_letter = self.letterPage.check_letter_by_inbox()
        ex_topic, ex_letter = ex_topic.text, ex_letter.text
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_header()
        self.letterPage.fill_letter()
        self.letterPage.close_letter()
        topic, letter = self.letterPage.check_letter_by_inbox()
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
        topic, letter = self.letterPage.check_draft()
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
        is_important = self.letterPage.check_importance()
        self.assertTrue(is_important)

    def test_notification_letter(self):
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_header()
        self.letterPage.fill_letter()
        self.letterPage.toggle_notification()
        self.letterPage.send_letter()
        self.letterPage.mark_letter_as_read()
        is_read = self.letterPage.check_read_status()
        self.assertTrue(is_read)
    
    def test_translate_letter(self):
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_header()
        is_translated = self.letterPage.translate_letter()
        self.assertTrue(is_translated)
    
    def test_cancel_translation(self):
        self.letterPage.click_on_new_letter_button()
        self.letterPage.fill_header()
        is_translated = self.letterPage.cancel_translation()
        self.assertFalse(is_translated)
    
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






    # def test_letter_update_notification(self):
    #     self.navbarPage.click_letter_icon()

    #     self.navbarPage.click_letter_link()

    #     self.letterPage.click_on_change_letter_link()

    #     self.assertEqual(self.letterPage.wait_for_update_button().text, 'ОБНОВИТЬ')

    #     self.letterPage.click_on_update_button()

    #     self.assertEqual(self.letterPage.wait_for_update_notification(), 'Данные обновлены!')

    # def test_update_all_positive(self):
    #     self.navbarPage.click_letter_icon()

    #     self.navbarPage.click_letter_link()

    #     self.letterPage.click_on_change_letter_link()

    #     # fill data

    #     self.letterPage.fill_name(NEW_NAME)

    #     self.letterPage.fill_surname(NEW_SURNAME)

    #     self.letterPage.fill_email(NEW_EMAIL)

    #     self.letterPage.select_sex(MALE_SEX)

    #     self.letterPage.fill_birthday(NEW_DATE)

    #     # click update

    #     self.letterPage.click_on_update_button()

    #     self.letterPage.refresh_page()

    #     # assert

    #     self.assertEqual(self.letterPage.get_updated_name(), NEW_NAME)

    #     self.assertEqual(self.letterPage.get_updated_surname(), NEW_SURNAME)

    #     self.assertEqual(self.letterPage.get_updated_email(), NEW_EMAIL)

    #     self.assertEqual(self.letterPage.get_updated_sex(), "Мужской")

    #     self.assertEqual(self.letterPage.get_updated_birthday(), NEW_DATE_COMPARE)

    #     def finalizer():
    #         self.letterPage.click_on_change_letter_link()
    #         self.letterPage.fill_name(OLD_NAME)

    #         self.letterPage.click_on_change_letter_link()
    #         self.letterPage.fill_surname(OLD_SURNAME)

    #         self.letterPage.click_on_change_letter_link()
    #         self.letterPage.fill_email(OLD_EMAIL)

    #         self.letterPage.select_sex(NO_SEX)

    #         self.letterPage.click_on_change_letter_link()
    #         self.letterPage.fill_birthday(OLD_DATE)

    #         self.letterPage.click_on_update_button()

    #     finalizer()

    def tearDown(self):
        self.driver.quit()
