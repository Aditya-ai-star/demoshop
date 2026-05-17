from pytest_bdd import scenarios, given, when, then
from pages.remove_cart_page import RemoveCartPage


scenarios("../features/remove_from_cart.feature")


@given("user has product in cart")
def add_product(browser):

    cart = RemoveCartPage(browser)

    cart.open_homepage()
    cart.add_product_to_cart()


@when("user removes product from cart")
def remove_product(browser):

    cart = RemoveCartPage(browser)

    cart.open_cart()
    cart.remove_product()


@then("cart should become empty")
def verify_empty_cart(browser):

    cart = RemoveCartPage(browser)

    assert cart.verify_cart_empty()