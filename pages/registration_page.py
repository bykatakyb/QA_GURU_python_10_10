import os

from selene import browser, be, have, command


class RegistrationPage:
    def __init__(self):
        self.subjects_input = browser.element('#subjectsInput')

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def fill_user_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    def choose_gender(self, value):
        browser.all('[for^=gender-radio]').element_by(have.exact_text(value)).click()

    def fill_phone_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    def fill_date_of_birth(self, year: int, month: int, day: int):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'[value="{year}"]').perform(command.js.scroll_into_view).click()
        browser.element('.react-datepicker__month-select').click().element(f'[value="{month - 1}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def choose_hobbies(self, *args):
        browser.element('[for=hobbies-checkbox-2]').perform(command.js.scroll_into_view)
        for hobby in args:
            browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text(hobby)).click()

    def upload_picture(self, value):
        browser.element('#uploadPicture').send_keys(os.path.abspath('image/image.jpg'))

    def fill_current_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)

    def fill_state(self, value):
        browser.element('#state').click()
        browser.all("[id^='react-select-3-option']").element_by(have.exact_text(value)).click()

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all("[id^='react-select-4-option']").element_by(have.exact_text(value)).click()

    def click_submit_button(self):
        browser.element('#submit').perform(command.js.click)

    def should_registered_user_with(self, first_name, last_name, email, gender, number, date_of_birth, subjects,
                                    hobbies, photo, current_address, state, city):
        browser.element('.modal-dialog').should(be.existing)
        browser.element(".table").all('td').even.should(
            have.exact_texts(
                f'{first_name} {last_name}',
                email,
                gender,
                number,
                date_of_birth,
                subjects,
                hobbies,
                photo,
                current_address,
                f'{state} {city}',
            ))
