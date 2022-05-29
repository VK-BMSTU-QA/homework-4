import unittest
from signin.signin import SignIn
from signup.signup import Signup
from basket.basket import Basket
from profile.profile import Profile
from one_product.one_product import OneProduct
from navbar.search_test import Search
from one_category.one_category import OneCategory


def suite():
    suite = unittest.TestSuite()
    suite.addTest(SignIn('test_signin_positive'))
    suite.addTest(SignIn('test_signin_empty_field'))
    suite.addTest(SignIn('test_signin_no_user'))
    suite.addTest(SignIn('test_signin_incorrect_password'))
    suite.addTest(SignIn('test_signin_short_password'))
    suite.addTest(SignIn('test_signin_redirect_to_signup'))

    suite.addTest(Signup('test_signup_positive'))
    suite.addTest(Signup('test_signup_empty_field'))
    suite.addTest(Signup('test_signup_user_exists'))
    suite.addTest(Signup('test_signup_passwords_not_match'))
    suite.addTest(Signup('test_signup_wrong_email_wrong'))
    suite.addTest(Signup('test_signup_redirect_to_signin'))

    suite.addTest(Basket('test_basket'))
    suite.addTest(Basket('test_basket_count'))
    suite.addTest(Basket('test_basket_empty'))
    suite.addTest(Basket('test_basket_change_sum_of_one_product'))
    suite.addTest(Basket('test_basket_change_sum_many_products'))
    suite.addTest(Basket('test_basket_selector'))
    suite.addTest(Basket('test_success_order'))

    suite.addTest(Profile('test_profile_update_notification'))
    suite.addTest(Profile('test_update_all'))

    suite.addTest(OneProduct('test_one_product_button_add_product'))
    suite.addTest(OneProduct('test_one_product_change_product_count'))
    suite.addTest(OneProduct('test_one_product_favourite_button_changes'))
    suite.addTest(OneProduct('test_one_product_add_favourite_product'))
    suite.addTest(OneProduct('test_one_product_review_appears'))
    suite.addTest(OneProduct('test_one_product_review_error_no_rating'))
    suite.addTest(OneProduct('test_one_product_review_error_no_text'))
    suite.addTest(OneProduct('test_one_product_redirect_to_catalog'))

    suite.addTest(Search('test_get_list_search'))
    suite.addTest(Search('test_click_on_product'))
    suite.addTest(Search('test_click_on_category'))
    suite.addTest(Search('test_input_text'))
    suite.addTest(Search('test_input_text_incorrect'))

    suite.addTest(OneCategory('test_sorting'))
    suite.addTest(OneCategory('test_filter_price_in_borders'))
    suite.addTest(OneCategory('test_filter_price_min_more_than_max'))
    suite.addTest(OneCategory('test_filter_price_max_less_than_min'))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
