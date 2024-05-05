import os

from selene import browser, have, be, command


def test_filling_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').should(be.blank).type('Cortny')
    browser.element('#lastName').should(be.blank).type('Love')

    browser.element('#userEmail').should(be.blank).type('CLU@mail.com')

    browser.element('[for="gender-radio-2"]').click()

    browser.element('#userNumber').should(be.blank).type('3133265290')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').element(f'option[value="7"]').click()
    browser.element('.react-datepicker__year-select').element(f'option[value="1991"]').click()
    browser.element('.react-datepicker__day--029:not(.react-datepicker__day--outside-month)').click()

    browser.element('#subjectsInput').type('Maths').press_enter()

    browser.element("label[for='hobbies-checkbox-2']").click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('image/image.jpg'))

    browser.element('#currentAddress').type('Javakhishvili St, 47, ap 39')

    browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').perform(command.js.click)
    browser.element('#city').click()
    browser.element('#react-select-4-option-2').perform(command.js.click)

    browser.element('#submit').perform(command.js.click)

    browser.element('.table').all('td').even.should(have.exact_texts(
        'Cortny Love',
        'CLU@mail.com',
        'Female',
        '3133265290',
        '29 August,1991',
        'Maths',
        'Reading',
        'image.jpg',
        'Javakhishvili St, 47, ap 39',
        'NCR Noida'))
