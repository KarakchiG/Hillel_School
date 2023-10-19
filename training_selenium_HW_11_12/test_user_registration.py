import allure
import requests
import pytest
from selenium import webdriver
from training_selenium_HW_11_12.facade.registration_facade import RegistrationFacade
from training_selenium_HW_11_12.factories.user_factory import generate_user_data


class TestBase:
    def setup_method(self):
        self._driver = webdriver.Chrome()
        self._session = requests.session()
        self._registration_facade = RegistrationFacade(self._driver)
        self._driver.implicitly_wait(3)
        self._driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")


class TestRegistration(TestBase):
    user_credentials = []

    def teardown_method(self):
        credentials = self.user_credentials.pop()
        self._sign_out(credentials=credentials)

    def _sign_out(self, credentials):
        self._session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=credentials)
        self._session.delete("https://qauto2.forstudy.space/api/users")
        self._driver.quit()

    @pytest.mark.parametrize("user", [generate_user_data() for _ in range(5)])
    def test_registration_test(self, user):
        self._registration_facade.register_user(**user)
        assert self._registration_facade.check_is_user_logged_in()

        credentials = dict(
            email=user["email"],
            password=user["password"],
            remember=False
        )
        self.user_credentials.append(credentials)
