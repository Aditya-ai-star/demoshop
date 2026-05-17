import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage:

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

    SUCCESS_MESSAGE = (
        By.CLASS_NAME,
        "result"
    )

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_register_page(self):

        self.driver.get(
            "https://demowebshop.tricentis.com/register"
        )

    def enter_registration_details(self):

        self.wait.until(
            EC.presence_of_element_located(
                self.GENDER
            )
        ).click()

        self.driver.find_element(
            *self.FIRST_NAME
        ).send_keys("Aditya")

        self.driver.find_element(
            *self.LAST_NAME
        ).send_keys("Raj")

        random_number = random.randint(
            1000,
            99999
        )

        email = f"aditya{random_number}@gmail.com"

        self.driver.find_element(
            *self.EMAIL
        ).send_keys(email)

        self.driver.find_element(
            *self.PASSWORD
        ).send_keys("Pass@123")

        self.driver.find_element(
            *self.CONFIRM_PASSWORD
        ).send_keys("Pass@123")

    def click_register(self):

        register = self.wait.until(
            EC.presence_of_element_located(
                self.REGISTER_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            register
        )

    def verify_registration(self):

        success = self.wait.until(
            EC.visibility_of_element_located(
                self.SUCCESS_MESSAGE
            )
        )

        return (
            "Your registration completed"
            in success.text
        )