from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductDetailsPage:

    PRODUCT_TITLE = (
        By.CLASS_NAME,
        "product-name"
    )

    PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        "span.price-value"
    )

    ADD_TO_CART = (
        By.ID,
        "add-to-cart-button-31"
    )

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_product_page(self):

        self.driver.get(
            "https://demowebshop.tricentis.com/141-inch-laptop"
        )

    def verify_product_title(self):

        title = self.wait.until(
            EC.visibility_of_element_located(
                self.PRODUCT_TITLE
            )
        )

        return (
            "14.1-inch Laptop"
            in title.text
        )

   
    def verify_add_to_cart(self):

        button = self.wait.until(
            EC.visibility_of_element_located(
                self.ADD_TO_CART
            )
        )

        return button.is_displayed()