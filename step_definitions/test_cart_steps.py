from pytest_bdd import scenarios, given, when, then
from pages.cart_page import CartPage


scenarios("../features/cart.feature")


@given("user opens homepage")
def open_homepage(browser):
    cart = CartPage(browser)
    cart.open_homepage()


@when("user adds product to cart")
def add_product(browser):
    cart = CartPage(browser)
    cart.add_product_to_cart()


@then("product should be added successfully")
def verify_cart(browser):
    cart = CartPage(browser)

    assert cart.verify_success_message()
