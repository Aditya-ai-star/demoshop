from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.login-button")
    LOGOUT_LINK = (By.LINK_TEXT, "Log out")

    
    def open(self):
        self.open_url(
            "https://demowebshop.tricentis.com/login"
        )

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_logout_visible(self):
        return self.driver.find_element(*self.LOGOUT_LINK).is_displayed()