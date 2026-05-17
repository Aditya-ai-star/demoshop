from pytest_bdd import scenarios, given, when, then
from pages.product_sorting_page import ProductSortingPage


scenarios("../features/product_sorting.feature")


@given("user is on category page")
def open_category(browser):

    sorting = ProductSortingPage(browser)

    sorting.open_category_page()


@when("user sorts products by price low to high")
def sort_products(browser):

    sorting = ProductSortingPage(browser)

    sorting.sort_products()


@then("products should be sorted successfully")
def verify_sorting(browser):

    sorting = ProductSortingPage(browser)

    assert sorting.verify_sorting()