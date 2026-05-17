from pytest_bdd import scenarios, given, when, then
from pages.register_page import RegisterPage


scenarios("../features/register.feature")


@given("user opens registration page")
def open_register(browser):

    register = RegisterPage(browser)

    register.open_register_page()


@when("user enters registration details")
def enter_details(browser):

    register = RegisterPage(browser)

    register.enter_registration_details()


@when("user clicks register button")
def click_register(browser):

    register = RegisterPage(browser)

    register.click_register()


@then("user should register successfully")
def verify_register(browser):

    register = RegisterPage(browser)

    assert register.verify_registration()