from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class BillingAddressPage:

    EMAIL = (By.ID, "Email")

    PASSWORD = (By.ID, "Password")

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "input.login-button"
    )

    BOOK_PRODUCT = (
        By.LINK_TEXT,
        "14.1-inch Laptop"
    )

    ADD_TO_CART = (
        By.CSS_SELECTOR,
        "input[value='Add to cart']"
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

    CONTINUE_BUTTON = (
        By.CSS_SELECTOR,
        "input.button-1.new-address-next-step-button"
    )

    BILLING_SECTION = (
        By.ID,
        "billing-buttons-container"
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

    def add_product_to_cart(self):

        product = self.wait.until(
            EC.presence_of_element_located(
                self.BOOK_PRODUCT
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            product
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

    def proceed_to_checkout(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.SHOPPING_CART
            )
        ).click()

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

    def enter_billing_address(self):

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
            print("Existing billing address already selected")  

    def save_billing_address(self):

        continue_button = self.wait.until(
            EC.presence_of_element_located(
                self.CONTINUE_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            continue_button
        )

    def verify_billing_address_saved(self):

        billing = self.wait.until(
            EC.visibility_of_element_located(
                self.BILLING_SECTION
            )
        )

        return billing.is_displayed()