from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class PaymentMethodPage:

    EMAIL = (By.ID, "Email")

    PASSWORD = (By.ID, "Password")

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "input.login-button"
    )

    PRODUCT = (
        By.LINK_TEXT,
        "Blue Jeans"
    )

    ADD_TO_CART = (
        By.XPATH,
        "//input[contains(@class,'add-to-cart-button')]"
    )

    SHOPPING_CART = (
        By.LINK_TEXT,
        "Shopping cart"
    )

    TERMS_CHECKBOX = (
        By.ID,
        "termsofservice"
    )

    CHECKOUT_BUTTON = (
        By.ID,
        "checkout"
    )

    BILLING_CONTINUE = (
        By.CSS_SELECTOR,
        "input.button-1.new-address-next-step-button"
    )

    SHIPPING_CONTINUE = (
        By.CSS_SELECTOR,
        "input.button-1.shipping-method-next-step-button"
    )

    PAYMENT_METHOD_RADIO = (
        By.ID,
        "paymentmethod_1"
    )

    PAYMENT_CONTINUE = (
        By.CSS_SELECTOR,
        "input.button-1.payment-method-next-step-button"
    )

    PAYMENT_INFO_SECTION = (
        By.CLASS_NAME,
        "payment-info"
    )

    COUNTRY = (
        By.ID,
        "BillingNewAddress_CountryId"
    )

    CITY = (
        By.ID,
        "BillingNewAddress_City"
    )

    ADDRESS1 = (
        By.ID,
        "BillingNewAddress_Address1"
    )

    ZIP_CODE = (
        By.ID,
        "BillingNewAddress_ZipPostalCode"
    )

    PHONE_NUMBER = (
        By.ID,
        "BillingNewAddress_PhoneNumber"
    )

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_login_page(self):

        self.driver.get(
            "https://demowebshop.tricentis.com/login"
        )

    def login(self):

        self.wait.until(
            EC.visibility_of_element_located(
                self.EMAIL
            )
        ).send_keys("ram444@gmail.com")

        self.driver.find_element(
            *self.PASSWORD
        ).send_keys("ramram")

        self.driver.find_element(
            *self.LOGIN_BUTTON
        ).click()

    def add_product(self):

        self.driver.get(
            "https://demowebshop.tricentis.com/blue-jeans"
        )

        add_cart = self.wait.until(
            EC.presence_of_element_located(
                self.ADD_TO_CART
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add_cart
        )

    def proceed_checkout(self):

        self.driver.get(
            "https://demowebshop.tricentis.com/cart"
        )

        checkbox = self.wait.until(
            EC.presence_of_element_located(
                self.TERMS_CHECKBOX
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            checkbox
        )

        checkout = self.wait.until(
            EC.presence_of_element_located(
                self.CHECKOUT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            checkout
        )

    def fill_billing_address(self):

        try:

            country = Select(
                self.wait.until(
                    EC.visibility_of_element_located(
                        self.COUNTRY
                    )
                )
            )

            country.select_by_visible_text("India")

            self.driver.find_element(
                *self.CITY
            ).send_keys("Bhopal")

            self.driver.find_element(
                *self.ADDRESS1
            ).send_keys("MP Nagar")

            self.driver.find_element(
                *self.ZIP_CODE
            ).send_keys("462001")

            self.driver.find_element(
                *self.PHONE_NUMBER
            ).send_keys("9876543210")

        except:
            print("Existing billing address selected")

    def continue_billing(self):

        continue_button = self.wait.until(
            EC.presence_of_element_located(
                self.BILLING_CONTINUE
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            continue_button
        )

    def complete_checkout_steps(self):

        try:

            shipping_method = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//input[@name='shippingoption']"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                shipping_method
            )

       

            shipping_continue = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        "input.button-1.shipping-method-next-step-button"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                shipping_continue
            )

        except:
            print("Shipping method skipped")

        try:

            payment_method = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//input[@name='paymentmethod']"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                payment_method
            )

            payment_continue = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        "input.button-1.payment-method-next-step-button"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                payment_continue
            )

        except:
            print("Payment method skipped")

        try:

            payment_info = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        "input.button-1.payment-info-next-step-button"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                payment_info
            )

        except:
            print("Payment info skipped")
            

    def verify_payment_method(self):

        current_url = self.driver.current_url

        return "checkout" in current_url