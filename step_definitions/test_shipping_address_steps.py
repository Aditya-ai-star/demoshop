from pytest_bdd import scenarios, given, when, then
from pages.shipping_address_page import ShippingAddressPage


scenarios("../features/shipping_address.feature")


@given("user is on checkout page")
def checkout_page(browser):

    shipping = ShippingAddressPage(browser)

    shipping.open_login_page()
    shipping.login()
    shipping.add_product()
    shipping.proceed_checkout()


@when("user enters shipping address")
def enter_shipping(browser):

    shipping = ShippingAddressPage(browser)

    shipping.fill_billing_address()
    shipping.continue_billing()


@then("shipping address should be saved")
def verify_shipping(browser):

    shipping = ShippingAddressPage(browser)

    assert shipping.verify_shipping_address()