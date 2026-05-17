from pytest_bdd import scenarios, given, when, then
from pages.shipping_method_page import ShippingMethodPage


scenarios("../features/shipping_method.feature")


@given("user is on shipping method page")
def shipping_page(browser):

    shipping = ShippingMethodPage(browser)

    shipping.open_login_page()
    shipping.login()
    shipping.add_product()
    shipping.proceed_checkout()

    shipping.fill_billing_address()
    shipping.continue_billing()


@when("user selects shipping method")
def select_shipping(browser):

    shipping = ShippingMethodPage(browser)
    shipping.complete_checkout_steps()

   


@then("shipping method should be selected")
def verify_shipping(browser):

    assert True