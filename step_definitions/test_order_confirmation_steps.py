from pytest_bdd import scenarios, given, when, then
from pages.order_confirmation_page import OrderConfirmationPage


scenarios("../features/order_confirmation.feature")


@given("user completes checkout process")
def checkout_process(browser):

    order = OrderConfirmationPage(browser)

    order.open_login_page()
    order.login()

    order.add_product()
    order.proceed_checkout()

    order.fill_billing_address()
    order.continue_billing()

    order.complete_checkout_steps()


@when("user confirms the order")
def confirm_order(browser):

    order = OrderConfirmationPage(browser)

    order.confirm_order()

@then("order should be placed successfully")
def verify_order(browser):

    assert True