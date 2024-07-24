# tests/test_pom.py
from selenium import webdriver
import pytest
from tests.pages.login_page import LoginPage
from tests.pages.search_page import SearchPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    yield driver

def test_login(driver):
    # Test the method of open page
    url = "https://practicetestautomation.com/practice-test-login/"
    LoginPage(driver).open_page(url)

    # Test the method of login
    username = "student"
    password = "Password123"
    LoginPage(driver).login_username(username)
    LoginPage(driver).login_password(password)
    LoginPage(driver).login_submit()

    # Test to verify the successful login
    LoginPage(driver).verify_successful_login()

def test_searching_box(driver):

    #Test the mode of open page
    url = "https://duckduckgo.com/"
    search_term = "Pytest with Eric"

    SearchPage(driver).open_web_page(url)

    # Test the search term
    #SearchPage(driver).search_page(search_term)
    
    # Test to submit the searching
    SearchPage(driver).search_page(search_term)

    SearchPage(driver).verify_searching_page(search_term)


