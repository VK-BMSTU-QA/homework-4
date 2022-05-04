from Base.BasePage import Page
from Profile.ProfileComponents import ProfileForm
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests.utils import CHECK_FREQ, TIMEOUT


class ProfilePage(Page):
    PATH = "profile"

    @property
    def profile_form(self):
        return ProfileForm(self.driver)

    def open(self):
        super().open()
        WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            EC.presence_of_element_located((By.CLASS_NAME, "profile-page"))
        )
