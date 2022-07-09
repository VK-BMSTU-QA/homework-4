import unittest
from letter.letter_test import Letter


def suite():
    suite = unittest.TestSuite()

    suite.addTest(Letter('test_default_letter'))
    # suite.addTest(Letter('test_send_letter_with_no_receiver'))
    # suite.addTest(Letter('test_send_letter_without_topic'))
    # suite.addTest(Letter('test_send_empty_letter'))
    # suite.addTest(Letter('test_cancel_letter'))
    # suite.addTest(Letter('test_add_to_templates'))
    # suite.addTest(Letter('test_resize_new_letter_popup'))
    # suite.addTest(Letter('test_close_letter'))
    # suite.addTest(Letter('test_collapse_then_expand_letter'))
    # suite.addTest(Letter('test_collapse_then_check_draft'))
    # suite.addTest(Letter('test_offer_call'))
    # suite.addTest(Letter('test_important_letter'))
    # suite.addTest(Letter('test_notification_letter'))
    # suite.addTest(Letter('test_translate_letter'))
    # suite.addTest(Letter('test_cancel_translation'))
    # suite.addTest(Letter('test_insert_signature'))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
