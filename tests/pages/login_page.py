# tests/pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class LoginPage:
    # Constructor of login page
    def __init__(self, driver):
        self.driver = driver

    # Method which allow to open a page
    def open_page(self, url):
        self.driver.get(url)

    # Method which find the username input and fill it
    def login_username(self, username):
        self.driver.find_element(By.ID,"username").send_keys(username)

    # Method which find the password input and fill it
    def login_password(self,password):
        self.driver.find_element(By.ID,"password").send_keys(password)

    # Method which find the submit button and click on
    def login_submit(self):
        self.driver.find_element(By.ID,"submit").click()

    # Method which verify the successful login or not
    def verify_successful_login(self):
        try:
            logout_button = self.driver.find_element(By.LINK_TEXT,"Log out")
            return logout_button.is_displayed()
        except NoSuchElementException:
            assert False, "Logout button does not exist."


