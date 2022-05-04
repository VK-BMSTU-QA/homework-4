from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Base.BasePage import Page
from Profile.ProfileComponents import ProfileForm


class ProfilePage(Page):
    PATH = 'profile'

    @property
    def profile_form(self):
        return ProfileForm(self.driver)

    def open(self):
        super().open()
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'profile-page'))
        )
