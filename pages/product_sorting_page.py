from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ProductSortingPage(BasePage):

    SORT_DROPDOWN = (
        By.ID,
        "products-orderby"
    )

    PRODUCT_PRICES = (
        By.CLASS_NAME,
        "price.actual-price"
    )

    

    def open_category_page(self):

        self.open_url(
            "https://demowebshop.tricentis.com/apparel-shoes"
        )

    def sort_products(self):

        dropdown = Select(
            self.wait.until(
                EC.presence_of_element_located(
                    self.SORT_DROPDOWN
                )
            )
        )

        dropdown.select_by_visible_text(
            "Price: Low to High"
        )

    def verify_sorting(self):

        self.wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.CSS_SELECTOR,
                    "span.price.actual-price"
                )
            )
        )

        prices = self.driver.find_elements(
            By.CSS_SELECTOR,
            "span.price.actual-price"
        )

        price_list = []

        for price in prices:

            value = price.text.replace(
                "$",
                ""
            )

            price_list.append(
                float(value)
            )

        sorted_prices = sorted(price_list)

        return price_list == sorted_prices