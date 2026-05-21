from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LogoutPage(BasePage):

    EMAIL = (
        By.ID,
        "Email"
    )

    PASSWORD = (
        By.ID,
        "Password"
    )

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "input.login-button"
    )

    LOGOUT_LINK = (
        By.LINK_TEXT,
        "Log out"
    )

    LOGIN_LINK = (
        By.LINK_TEXT,
        "Log in"
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

    def click_logout(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.LOGOUT_LINK
            )
        ).click()

    def verify_logout(self):

        login_link = self.wait.until(
            EC.visibility_of_element_located(
                self.LOGIN_LINK
            )
        )

        return login_link.is_displayed()