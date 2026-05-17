from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactUsPage:

    ENQUIRY = (
        By.ID,
        "Enquiry"
    )

    SUBMIT_BUTTON = (
        By.NAME,
        "send-email"
    )

    SUCCESS_MESSAGE = (
        By.CLASS_NAME,
        "result"
    )

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_contact_page(self):

        self.driver.get(
            "https://demowebshop.tricentis.com/contactus"
        )

    def submit_contact_form(self):

        email = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.ID,
                    "FullName"
                )
            )
        )

        email.send_keys("Aditya Raj")

        self.driver.find_element(
            By.ID,
            "Email"
        ).send_keys("ram444@gmail.com")

        self.driver.find_element(
            *self.ENQUIRY
        ).send_keys(
            "This is automation testing enquiry"
        )

        submit = self.wait.until(
            EC.presence_of_element_located(
                self.SUBMIT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            submit
        )

    def verify_contact_submission(self):

        return "contactus" in self.driver.current_url