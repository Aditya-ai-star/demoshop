from selenium.webdriver.common.by import By


class LoginPage:

    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.login-button")
    LOGOUT_LINK = (By.LINK_TEXT, "Log out")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(
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