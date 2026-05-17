from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RemoveCartPage:

    PRODUCT = (
        By.LINK_TEXT,
        "Build your own cheap computer"
    )

    ADD_TO_CART_BUTTON = (
        By.CSS_SELECTOR,
        "input[value='Add to cart']"
    )

    SHOPPING_CART = (
        By.LINK_TEXT,
        "Shopping cart"
    )

    REMOVE_CHECKBOX = (
        By.XPATH,
        "//input[contains(@name,'removefromcart')]"
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

        self.driver.get(
            "https://demowebshop.tricentis.com/build-your-cheap-own-computer"
        )

        add_cart = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//input[contains(@class,'add-to-cart-button')]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add_cart
        )

        self.driver.get(
            "https://demowebshop.tricentis.com/cart"
        )

    def open_cart(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.SHOPPING_CART
            )
        ).click()

    def remove_product(self):

        try:

            remove_checkbox = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//input[contains(@name,'removefromcart')]"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                remove_checkbox
            )

            update_button = self.wait.until(
                EC.presence_of_element_located(
                    self.UPDATE_CART_BUTTON
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                update_button
            )

        except:
            print("Cart already empty")

            
    def verify_cart_empty(self):

        message = self.wait.until(
            EC.visibility_of_element_located(
                self.EMPTY_CART_MESSAGE
            )
        )

        return "Your Shopping Cart is empty!" in message.text