from pytest_bdd import scenarios, given, when, then
from pages.payment_information_page import PaymentInformationPage


scenarios("../features/payment_information.feature")


@given("user is on payment information page")
def payment_info_page(browser):

    payment = PaymentInformationPage(browser)

    payment.open_login_page()
    payment.login()

    payment.add_product()
    payment.proceed_checkout()

    payment.fill_billing_address()
    payment.continue_billing()

    payment.complete_checkout_steps()


@when("user continues payment information")
def continue_payment(browser):

    payment = PaymentInformationPage(browser)

    payment.continue_payment_information()


@then("payment information should be processed")
def verify_payment(browser):

    payment = PaymentInformationPage(browser)

    assert payment.verify_payment_information()