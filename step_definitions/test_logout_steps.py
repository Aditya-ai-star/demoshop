from pytest_bdd import scenarios, given, when, then
from pages.logout_page import LogoutPage


scenarios("../features/logout.feature")


@given("user logs into application")
def login_user(browser):

    logout = LogoutPage(browser)

    logout.open_login_page()
    logout.login()


@when("user clicks logout button")
def click_logout(browser):

    logout = LogoutPage(browser)

    logout.click_logout()


@then("user should logout successfully")
def verify_logout(browser):

    logout = LogoutPage(browser)

    assert logout.verify_logout()