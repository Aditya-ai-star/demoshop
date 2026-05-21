from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExistingUserRegistrationPage:

    GENDER = (
        By.ID,
        "gender-male"
    )

    FIRST_NAME = (
        By.ID,
        "FirstName"
    )

    LAST_NAME = (
        By.ID,
        "LastName"
    )

    EMAIL = (
        By.ID,
        "Email"
    )

    PASSWORD = (
        By.ID,
        "Password"
    )

    CONFIRM_PASSWORD = (
        By.ID,
        "ConfirmPassword"
    )

    REGISTER_BUTTON = (
        By.ID,
        "register-button"
    )

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "div.validation-summary-errors"
    )

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_register_page(self):

        self.driver.get(
            "https://demowebshop.tricentis.com/register"
        )

    def enter_existing_user_details(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.GENDER
            )
        ).click()

        self.driver.find_element(
            *self.FIRST_NAME
        ).send_keys("Aditya")

        self.driver.find_element(
            *self.LAST_NAME
        ).send_keys("Raj")

        self.driver.find_element(
            *self.EMAIL
        ).send_keys("ram444@gmail.com")

        self.driver.find_element(
            *self.PASSWORD
        ).send_keys("Pass@123")

        self.driver.find_element(
            *self.CONFIRM_PASSWORD
        ).send_keys("Pass@123")

    def click_register(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.REGISTER_BUTTON
            )
        ).click()

    def verify_registration_failed(self):

        error = self.wait.until(
            EC.visibility_of_element_located(
                self.ERROR_MESSAGE
            )
        )

        return (
            "The specified email already exists"
            in error.text
        )