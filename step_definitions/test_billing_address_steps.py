from pytest_bdd import scenarios, given, when, then
from pages.billing_address_page import BillingAddressPage


scenarios("../features/billing_address.feature")


@given("user proceeds to checkout")
def proceed_checkout(browser):

    billing = BillingAddressPage(browser)

    billing.open_login_page()
    billing.login()
    billing.add_product_to_cart()
    billing.proceed_to_checkout()


@when("user enters billing address")
def enter_address(browser):

    billing = BillingAddressPage(browser)

    billing.enter_billing_address()
    billing.save_billing_address()


@then("billing address should be saved")
def verify_billing(browser):

    billing = BillingAddressPage(browser)

    assert billing.verify_billing_address_saved()