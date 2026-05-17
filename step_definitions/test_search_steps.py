from pytest_bdd import scenarios, given, when, then
from pages.search_page import SearchPage


scenarios("../features/search_product.feature")


@given("user is on homepage")
def open_homepage(browser):
    search = SearchPage(browser)
    search.open_homepage()


@when("user searches for product")
def search_product(browser):
    search = SearchPage(browser)

    search.search_product(
        "Build your own cheap computer"
    )


@then("searched product should be displayed")
def verify_product(browser):
    search = SearchPage(browser)

    assert search.is_product_displayed()