from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RemoveCartPage:

    PRODUCT = (
        By.LINK_TEXT,
        "Build your own cheap computer"
    )

    ADD_TO_CART_BUTTON = (
        By.ID,
        "add-to-cart-button-72"
    )

    SHOPPING_CART = (
        By.LINK_TEXT,
        "Shopping cart"
    )

    REMOVE_CHECKBOX = (
        By.NAME,
        "removefromcart"
    )

    UPDATE_CART_BUTTON = (
        By.NAME,
        "updatecart"
    )

    EMPTY_CART_MESSAGE = (
        By.CSS_SELECTOR,
        "div.order-summary-content"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_homepage(self):
        self.driver.get(
            "https://demowebshop.tricentis.com/"
        )

    def add_product_to_cart(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.PRODUCT
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_TO_CART_BUTTON
            )
        ).click()

    def open_cart(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.SHOPPING_CART
            )
        ).click()

    def remove_product(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.REMOVE_CHECKBOX
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                self.UPDATE_CART_BUTTON
            )
        ).click()

    def verify_cart_empty(self):

        message = self.wait.until(
            EC.visibility_of_element_located(
                self.EMPTY_CART_MESSAGE
            )
        )

        return "Your Shopping Cart is empty!" in message.text