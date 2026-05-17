from pytest_bdd import scenarios, given, then
from pages.product_details_page import ProductDetailsPage


scenarios("../features/product_details.feature")


@given("user opens product details page")
def open_product(browser):

    product = ProductDetailsPage(browser)

    product.open_product_page()


@then("product details should be displayed correctly")
def verify_product(browser):

    product = ProductDetailsPage(browser)

    assert product.verify_product_title()
    assert product.verify_add_to_cart()