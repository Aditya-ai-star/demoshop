from pytest_bdd import scenarios, given, when, then
from pages.invalid_login_page import InvalidLoginPage


scenarios("../features/invalid_login.feature")


@given("user opens login page for invalid login")
def open_login(browser):

    login = InvalidLoginPage(browser)

    login.open_login_page()


@when("user enters invalid email and password")
def invalid_credentials(browser):

    login = InvalidLoginPage(browser)

    login.enter_invalid_credentials()


@when("user clicks login button for invalid login")
def click_login(browser):

    login = InvalidLoginPage(browser)

    login.click_login()


@then("error message should be displayed")
def verify_error(browser):

    login = InvalidLoginPage(browser)

    assert login.verify_error_message()