from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage


scenarios("../features/login.feature")


@given("user opens login page")
def open_login_page(browser):
    login = LoginPage(browser)
    login.open()


@when("user enters valid email and password")
def enter_credentials(browser):
    login = LoginPage(browser)

    login.enter_email("ram444@gmail.com")
    login.enter_password("ramram")


@when("user clicks login button")
def click_login(browser):
    login = LoginPage(browser)
    login.click_login()


@then("user should login successfully")
def verify_login(browser):
    login = LoginPage(browser)

    assert login.is_logout_visible()