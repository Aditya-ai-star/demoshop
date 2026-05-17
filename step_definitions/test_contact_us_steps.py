from pytest_bdd import scenarios, given, when, then
from pages.contact_us_page import ContactUsPage


scenarios("../features/contact_us.feature")


@given("user opens contact us page")
def open_contact(browser):

    contact = ContactUsPage(browser)

    contact.open_contact_page()


@when("user submits contact form")
def submit_form(browser):

    contact = ContactUsPage(browser)

    contact.submit_contact_form()


@then("contact form should be submitted successfully")
def verify_submission(browser):

    contact = ContactUsPage(browser)

    assert contact.verify_contact_submission()