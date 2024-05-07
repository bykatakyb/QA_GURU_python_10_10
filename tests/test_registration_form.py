from data import users
from pages.registration_page import RegistrationPage


def test_filling_form():
    cortny = users.cortny
    registration_page = RegistrationPage()
    # pre-conditions
    registration_page.open()
    # WHEN
    registration_page.make_registration_by_user(cortny)
    # THEN
    registration_page.should_registered_user_with(cortny)
