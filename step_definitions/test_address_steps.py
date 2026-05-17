from pytest_bdd import scenarios, given, when, then
from pages.address_page import AddressPage


scenarios("../features/address_management.feature")


@given("user is logged in")
def login_user(browser):

    address = AddressPage(browser)

    address.open_login_page()
    address.login()


@when("user adds new address")
def add_new_address(browser):

    address = AddressPage(browser)

    address.open_addresses()
    address.click_add_new_address()
    address.fill_address_form()


@when("user saves address")
def save_address(browser):

    address = AddressPage(browser)

    address.save_address()


@then("address should be added successfully")
def verify_address(browser):

    address = AddressPage(browser)

    assert address.verify_address_added()