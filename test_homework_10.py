import pytest
import requests
from hamcrest import *

base_url = "https://qauto2.forstudy.space/api"


class UserSignUpSchema:

    def __init__(self, name, last_name, email, password, repeat_password):
        self.name = name
        self.lastName = last_name
        self.email = email
        self.password = password
        self.repeatPassword = repeat_password


class UserSignInSchema:

    def __init__(self, email, password, remember):
        self.email = email
        self.password = password
        self.remember = remember


class TestUserCreation:

    def setup_class(self):
        self.user_to_sign_up = UserSignUpSchema("Gena", "Karakchi", "karakchigena@ggtest.com", "Qwerty1234",
                                                "Qwerty1234")

    def setup_method(self):
        self.session = requests.session()

    def test_user_creation(self):
        user_creation = self.session.post(url=f"{base_url}/auth/signup", json=self.user_to_sign_up.__dict__)

        assert_that(user_creation.status_code, equal_to(201))

        data = user_creation.json()
        assert_that(data["status"], equal_to("ok"))
        assert_that(data["data"], has_key("distanceUnits"))
        assert_that(data["data"], has_key("currency"))

    def teardown_method(self):
        self.session.delete(f"{base_url}/users")


class TestUserSignIn:

    def setup_class(self):
        self.user_to_sign_up = UserSignUpSchema("Gena", "Karakchi", "karakchigena@ggtest.com", "Qwerty1234",
                                                "Qwerty1234")

        self.user_to_sign_in = UserSignInSchema("karakchigena@ggtest.com", "Qwerty1234", False)

    def setup_method(self):
        self.session = requests.session()

        self.session.post(url=f"{base_url}/auth/signup", json=self.user_to_sign_up.__dict__)

    def test_user_sign_in(self):
        user_sign_in = self.session.post(url=f"{base_url}/auth/signin", json=self.user_to_sign_in.__dict__)

        assert_that(user_sign_in.status_code, equal_to(200))

        data = user_sign_in.json()
        assert_that(data["status"], equal_to("ok"))
        assert_that(data["data"], has_key("distanceUnits"))
        assert_that(data["data"], has_key("currency"))

    def teardown_method(self):
        self.session.delete(f"{base_url}/users")


class TestUserProfile:
    def setup_class(self):
        self.user_to_sign_up = UserSignUpSchema("Gena", "Karakchi", "karakchigena@ggtest.com", "Qwerty1234",
                                                "Qwerty1234")

    def setup_method(self):
        self.session = requests.session()

        self.session.post(url=f"{base_url}/auth/signup", json=self.user_to_sign_up.__dict__)

    def test_user_profile(self):
        user_profile = self.session.get(f"{base_url}/users/profile")

        assert_that(user_profile.status_code, equal_to(200))

        data = user_profile.json()
        assert_that(data["status"], equal_to("ok"))
        assert_that(data["data"]["name"], equal_to("Gena"))
        assert_that(data["data"]["lastName"], equal_to("Karakchi"))

    def teardown_method(self):
        self.session.delete(f"{base_url}/users")


class TestUserPassword:
    def setup_class(self):
        self.user_to_sign_up = UserSignUpSchema("Gena", "Karakchi", "karakchigena@ggtest.com", "Qwerty1234",
                                                "Qwerty1234")

    def setup_method(self):
        self.session = requests.session()

        self.session.post(url=f"{base_url}/auth/signup", json=self.user_to_sign_up.__dict__)

    @pytest.mark.parametrize("user, expected_status_code, expected_status", [
                (UserSignInSchema("karakchigena@ggtest.com", "Qwerty1234", False), 200, "ok"),
                (UserSignInSchema("karakchigena@ggtest.com", "IncorrectPassword", False), 400, "error")
                             ])
    def test_user_sign_in(self, user, expected_status_code, expected_status):
        user_sign_in = self.session.post(url=f"{base_url}/auth/signin", json=user.__dict__)

        assert_that(user_sign_in.status_code, equal_to(expected_status_code))

        data = user_sign_in.json()
        assert_that(data["status"], equal_to(expected_status))

    def teardown_method(self):
        self.session.delete(f"{base_url}/users")
