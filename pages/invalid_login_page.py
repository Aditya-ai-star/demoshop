from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class InvalidLoginPage(BasePage):

    EMAIL = (By.ID, "Email")

    PASSWORD = (By.ID, "Password")

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "input.login-button"
    )

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "div.validation-summary-errors"
    )

    

    def open_login_page(self):

        self.open_url(
            "https://demowebshop.tricentis.com/login"
        )

    def enter_invalid_credentials(self):

        self.wait.until(
            EC.visibility_of_element_located(
                self.EMAIL
            )
        ).send_keys("wrong@gmail.com")

        self.driver.find_element(
            *self.PASSWORD
        ).send_keys("WrongPassword")

    def click_login(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.LOGIN_BUTTON
            )
        ).click()

    def verify_error_message(self):

        error = self.wait.until(
            EC.visibility_of_element_located(
                self.ERROR_MESSAGE
            )
        )

        return "Login was unsuccessful" in error.text