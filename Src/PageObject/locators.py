class Locator(object):
    create_account = "//button[text()='Create An Account']"

    first_name_input = "//input[@id='firstName']"
    last_name_input = "//input[@id='lastName']"

    email_input = "//input[@id='email']"

    password_input = "//input[@id='password']"
    confirm_password_input = "//input[@id='confirmPassword']"

    accredited_yes_radio = "//input[@id='accreditedYes']"
    accredited_no_radio = "//input[@id='accreditedNo']"

    tos_checkbox = "//input[@id='hasAgreedTos']"

    captcha_iframe = "iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']"

    main_iframe = "//iframe[@id='_hjRemoteVarsFrame']"

    submit_button = "//button[@data-testid='submit-button']"
