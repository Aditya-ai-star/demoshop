from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AddressPage(BasePage):

    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")

    LOGIN_BUTTON = (By.CSS_SELECTOR,"input.login-button")

    MY_ACCOUNT = (By.LINK_TEXT,"My account")

    ADDRESSES_LINK = (By.LINK_TEXT,"Addresses")

    ADD_NEW_BUTTON = (
        By.CSS_SELECTOR,
        "input.button-1.add-address-button"
    )

    FIRST_NAME = (
        By.ID,
        "Address_FirstName"
    )

    LAST_NAME = (
        By.ID,
        "Address_LastName"
    )

    EMAIL_ADDRESS = (
        By.ID,
        "Address_Email"
    )

    COMPANY = (
        By.ID,
        "Address_Company"
    )

    COUNTRY = (
        By.ID,
        "Address_CountryId"
    )

    CITY = (
        By.ID,
        "Address_City"
    )

    ADDRESS1 = (
        By.ID,
        "Address_Address1"
    )

    ZIP_CODE = (
        By.ID,
        "Address_ZipPostalCode"
    )

    PHONE_NUMBER = (
        By.ID,
        "Address_PhoneNumber"
    )

    SAVE_BUTTON = (
        By.CSS_SELECTOR,
        "input.button-1.save-address-button"
    )

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        "div.section.address-item"
    )

    

    def open_login_page(self):

        self.open_url(
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


    def open_addresses(self):

        self.driver.get(
            "https://demowebshop.tricentis.com/customer/addresses"
        )

    """def open_addresses(self):

        my_account = self.wait.until(
            EC.presence_of_element_located(
                self.MY_ACCOUNT
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            my_account
        )

        addresses = self.wait.until(
            EC.presence_of_element_located(
                self.ADDRESSES_LINK
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            addresses
        )"""

    def click_add_new_address(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_NEW_BUTTON
            )
        ).click()

    def fill_address_form(self):

        self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_NAME
            )
        ).send_keys("Aditya")

        self.driver.find_element(
            *self.LAST_NAME
        ).send_keys("Raj")

        self.driver.find_element(
            *self.EMAIL_ADDRESS
        ).send_keys("ram444@gmail.com")

        self.driver.find_element(
            *self.COMPANY
        ).send_keys("Wipro")

        country = Select(
            self.driver.find_element(
                *self.COUNTRY
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

    def save_address(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.SAVE_BUTTON
            )
        ).click()

    def verify_address_added(self):

        success = self.wait.until(
            EC.visibility_of_element_located(
                self.SUCCESS_MESSAGE
            )
        )

        return success.is_displayed()