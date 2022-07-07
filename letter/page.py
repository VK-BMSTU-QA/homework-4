from base_page import BasePage
from letter.static_locators import *

import os


class LetterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_new_letter_button(self):
        new_letter_button = self.get_element_by_class(new_letter_locator)
        new_letter_button.click()

    def fill_header(self):
        receiver = os.environ.get('LOGIN')
        receiver_input = self.get_element_by_class(reciever_mail_locator)
        receiver_input.send_keys(receiver)
        topic = 'SAMPLE TEXT'
        topic_input = self.get_element_by_name(topic_mail_locator)
        topic_input.send_keys(topic)

    def fill_receiver(self):
        receiver = os.environ.get('LOGIN')
        receiver_input = self.get_element_by_class(reciever_mail_locator)
        receiver_input.send_keys(receiver)

    def fill_letter(self):
        text = 'SAMPLETEXT SAMPLETEXT SAMPLETEXT SAMPLETEXT'
        letter_input = self.get_element_by_class(letter_text_locator)
        letter_input.send_keys(text)

    def send_letter(self):
        send_button = self.get_element_by_class(send_button_locator)
        send_button.click()

    def cancel_letter(self):
        cancel_button = self.get_elements_by_class(cancel_button_locator)[2]
        cancel_button.click()

    def confirm_empty_letter(self):
        confirm_button = self.get_element_by_class(empty_letter_confirm_locator)
        confirm_button.click()

    def get_letter_by_inbox(self):
        self.driver.get('https://e.mail.ru/inbox/')
        letter = self.get_element_by_class(letter_locator)
        letter.click()
        topic = self.get_element_by_class(check_topic_locator)
        letter = self.get_element_by_class(check_letter_text_locator)
        return topic, letter

    def get_letter_by_sent(self):
        self.driver.get('https://e.mail.ru/sent/')
        letter = self.get_element_by_class(letter_locator)
        letter.click()
        topic = self.get_element_by_class(check_topic_locator)
        letter = self.get_element_by_class(check_letter_text_locator)
        return topic, letter

    def get_no_receiver_error(self):
        error = self.get_element_by_class(error_no_receiver_locator)
        return error

    def add_to_templates(self):
        button1 = self.get_element_by_class(template_button_in_letter_locator)
        button1.click()
        button2 = self.get_element_by_class(add_to_templates_button_locator)
        button2.click()

    def get_template(self):
        self.driver.get('https://e.mail.ru/templates/')
        template = self.get_element_by_class(template_locator)
        template.click()
        topic = self.get_element_by_name(topic_mail_locator)
        letter = self.get_element_by_class(letter_text_locator)
        return topic, letter

    def get_letter(self):
        topic = self.get_element_by_name(topic_mail_locator)
        letter = self.get_element_by_class(letter_text_locator)
        return topic, letter

    def resize_letter_popup(self):
        resize_button = self.get_elements_by_class(resize_button_locator)[1]
        resize_button.click()
        topic = self.get_element_by_name(topic_mail_locator)
        letter = self.get_element_by_class(letter_text_locator)
        return topic, letter

    def close_letter(self):
        close_button = self.get_elements_by_class(close_button_locator)[2]
        close_button.click()

    def collapse_letter(self):
        collapse_button = self.get_elements_by_class(collapse_button_locator)[0]
        collapse_button.click()

    def expand_letter(self):
        expand_button = self.get_element_by_class(expand_button_locator)
        expand_button.click()

    def get_draft(self):
        self.driver.get('https://e.mail.ru/drafts/')
        draft = self.get_element_by_class(draft_locator)
        draft.click()
        topic = self.get_element_by_name(topic_mail_locator)
        letter = self.get_element_by_class(letter_text_locator)
        return topic, letter

    def offer_call(self):
        offer_call_button = self.get_elements_by_class(offer_call_button_locator)[11]
        offer_call_button.click()
        self.wait_for_text_to_appear(letter_text_locator, 'Перейдите')
        letter = self.get_element_by_class(letter_text_locator)
        return letter

    def toggle_importance(self):
        toggle_importance_button = self.get_element_by_class(toggle_importance_button_locator)
        toggle_importance_button.click()

    def get_importance_status(self):
        self.driver.get('https://e.mail.ru/inbox/')
        letter = self.get_element_by_class(letter_locator)
        letter.click()
        return self.get_elements_by_class(importance_indicator_locator)

    def toggle_notification(self):
        toggle_notification_button = self.get_elements_by_class(toggle_notification_button_locator)[1]
        toggle_notification_button.click()

    def mark_letter_as_read(self):
        self.driver.get('https://e.mail.ru/inbox/')
        letter = self.get_element_by_class(letter_locator)
        letter.click()
        mark_as_read_button = self.get_element_by_class(mark_letter_as_read_locator)
        mark_as_read_button.click()

    def get_read_status(self):
        self.driver.get('https://e.mail.ru/inbox/')
        letter = self.get_element_by_class(letter_locator)
        letter.click()
        return self.get_element_by_class(notification_topic_locator)

    def translate_letter(self, text):
        letter_input = self.get_element_by_class(letter_text_locator)
        letter_input.send_keys(text)

        translate_button = self.get_elements_by_class(translate_button_locator)[28]
        translate_button.click()
        confirm_translation_button = self.get_elements_by_class(confirm_translation_locator)[0]
        confirm_translation_button.click()

        letter = self.get_element_by_class(letter_text_locator)
        return letter.text.split()[0]

    def cancel_translation(self, text):
        letter_input = self.get_element_by_class(letter_text_locator)
        letter_input.send_keys(text)

        translate_button = self.get_elements_by_class(translate_button_locator)[28]
        translate_button.click()
        cancel_translation_button = self.get_elements_by_class(cancel_translation_locator)[1]
        cancel_translation_button.click()

        letter = self.get_element_by_class(letter_text_locator)
        return letter.text.split()[0]

    def clear_format(self):
        clear_format_button = self.get_elements_by_class(clear_button_locator)[23]
        clear_format_button.click()
        confirm_clear_button = self.get_element_by_class(confirm_clear_button_locator)
        confirm_clear_button.click()

    def insert_signature(self):
        insert_format_button = self.get_elements_by_class(clear_button_locator)[24]
        insert_format_button.click()
