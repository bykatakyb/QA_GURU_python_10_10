from pages.registration_page import RegistrationPage


def test_filling_form():
    registration_page = RegistrationPage()
    # open form
    registration_page.open()
    # WHEN
    registration_page.fill_first_name('Cortny')
    registration_page.fill_last_name('Love')
    registration_page.fill_user_email('CLU@mail.com')
    registration_page.choose_gender('Female')
    registration_page.fill_phone_number('3133265290')
    registration_page.fill_date_of_birth(year=1991, month=9, day=29)
    registration_page.fill_subject('Maths')
    registration_page.choose_hobbies('Reading')
    registration_page.upload_picture('image.jpg') #'image/image.jpg'
    registration_page.fill_current_address('Javakhishvili St, 47, ap 39')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Noida')
    registration_page.click_submit_button()

    # THEN
    registration_page.should_registered_user_with(
        'Cortny',
        'Love',
        'CLU@mail.com',
        'Female',
        '3133265290',
        '29 September,1991',
        'Maths',
        'Reading',
        'image.jpg',
        'Javakhishvili St, 47, ap 39',
        'NCR',
        'Noida',
    )

