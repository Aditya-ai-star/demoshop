from pytest_bdd import (
    scenarios,
    given,
    when,
    then
)

from pages.existing_user_registration_page import (
    ExistingUserRegistrationPage
)


scenarios(
    "../features/existing_user_registration.feature"
)


@given("user is on register page")
def open_register(browser):

    register = ExistingUserRegistrationPage(
        browser
    )

    register.open_register_page()


@when("user enters already registered email")
def enter_existing_user(browser):

    register = ExistingUserRegistrationPage(
        browser
    )

    register.enter_existing_user_details()


@when("user clicks register button")
def click_register(browser):

    register = ExistingUserRegistrationPage(
        browser
    )

    register.click_register()


@then("registration should fail")
def verify_registration(browser):

    register = ExistingUserRegistrationPage(
        browser
    )

    assert register.verify_registration_failed()