import os

from selene import browser, be, have, command

from data.users import User, date


class RegistrationPage:
    def __init__(self):
        self.subjects_input = browser.element('#subjectsInput')

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, user: User):
        browser.element('#firstName').should(be.blank).type(user.first_name)

    def fill_last_name(self, user: User):
        browser.element('#lastName').should(be.blank).type(user.last_name)

    def fill_user_email(self, user: User):
        browser.element('#userEmail').should(be.blank).type(user.email)

    def choose_gender(self, user: User):
        browser.all('[for^=gender-radio]').element_by(have.exact_text(user.gender)).click()

    def fill_phone_number(self, user: User):
        browser.element('#userNumber').should(be.blank).type(user.phone_number)

    def fill_date_of_birth(self, user: User):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'[value="{user.birth_year}"]').perform(command.js.scroll_into_view).click()
        browser.element('.react-datepicker__month-select').click().element(f'[value="{user.birth_month - 1}"]').click()
        browser.element(f'.react-datepicker__day--0{user.birth_day}').click()

    def fill_subjects(self, user: User):
        self.subjects_input.should(be.blank).type(user.subjects[0]).press_enter()
        if len(user.subjects) >= 2:
            for sub in user.subjects[1:]:
                self.subjects_input.type(sub)
                browser.element('#react-select-2-option-0').click()

    def choose_hobbies(self, user: User):
        browser.element('[for=hobbies-checkbox-2]').perform(command.js.scroll_into_view)
        for hobby in user.hobbies:
            browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text(hobby)).click()

    def upload_picture(self, user: User):
        browser.element('#uploadPicture').send_keys(os.path.abspath(user.picture))

    def fill_current_address(self, user: User):
        browser.element('#currentAddress').should(be.blank).type(user.current_address)

    def fill_state(self, user: User):
        browser.element('#state').click()
        browser.all("[id^='react-select-3-option']").element_by(have.exact_text(user.state)).click()

    def fill_city(self, user: User):
        browser.element('#city').click()
        browser.all("[id^='react-select-4-option']").element_by(have.exact_text(user.city)).click()

    def click_submit_button(self):
        browser.element('#submit').perform(command.js.click)

    def make_registration_by_user(self, user: User):
        self.fill_first_name(user)
        self.fill_last_name(user)
        self.fill_user_email(user)
        self.choose_gender(user)
        self.fill_phone_number(user)
        self.fill_date_of_birth(user)
        self.fill_subjects(user)
        self.choose_hobbies(user)
        self.upload_picture(user)
        self.fill_current_address(user)
        self.fill_state(user)
        self.fill_city(user)
        self.click_submit_button()

    def should_registered_user_with(self, user: User):
        browser.element('.modal-dialog').should(be.existing)
        browser.element(".table").all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.phone_number,
                f"{user.birth_day} {date.strftime('%B')},{user.birth_year}",
                ', '.join(user.subjects),
                ', '.join(user.hobbies),
                user.picture,
                user.current_address,
                f'{user.state} {user.city}',
            ))
