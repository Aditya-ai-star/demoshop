from pytest_bdd import scenarios, given, when, then
from pages.payment_method_page import PaymentMethodPage


scenarios("../features/payment_method.feature")


@given("user is on payment page")
def payment_page(browser):

    payment = PaymentMethodPage(browser)

    payment.open_login_page()
    payment.login()

    payment.add_product()
    payment.proceed_checkout()

    payment.fill_billing_address()
    payment.continue_billing()

    payment.complete_checkout_steps()


@when("user selects payment method")
def select_payment(browser):

    payment = PaymentMethodPage(browser)

    payment.complete_checkout_steps()


@then("payment method should be selected")
def verify_payment(browser):

    payment = PaymentMethodPage(browser)

    assert payment.verify_payment_method()