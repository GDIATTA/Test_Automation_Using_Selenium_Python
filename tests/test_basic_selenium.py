import pytest  
from selenium import webdriver  
from selenium.webdriver.chrome.service import Service as ChromeService 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

#from webdriver_manager.chrome import ChromeDriverManager  
  
  
@pytest.fixture()  
def chrome_browser():  
    driver = webdriver.Chrome()  
  
    # Use this line instead of the prev if you wish to download the ChromeDriver binary on the fly  
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  
      
    driver.implicitly_wait(10)  
    # Yield the WebDriver instance  
    yield driver  
    # Close the WebDriver instance  
    #driver.quit()

def test_title(chrome_browser):

    # Test the title of Python.org website
    chrome_browser.get("https://www.python.org")
    assert chrome_browser.title == "Welcome to Python.org"

def test_search(chrome_browser):

    # Test the search functionality of the DuckDuckGo 
    # website
    url = "https://duckduckgo.com/"

    search_term = "Pytest with Eric"

    # Navigate to the web page
    chrome_browser.get(url)

    # Find the search box using its name attribute value
    #search_box = chrome_browser.find_element(By.ID,value="searchbox_input")
    # Wait for the search box to be present
    search_box = WebDriverWait(chrome_browser, 10).until(
        EC.presence_of_element_located((By.ID, "searchbox_input")))

    # Enter a search query and submit
    search_box.send_keys(search_term)
    search_box.submit()

    # Wait for the title to update
    WebDriverWait(chrome_browser, 10).until(
        EC.title_contains(search_term)
    )
    
    # Assert that the title contains the search term.  
    assert search_term in chrome_browser.title

def test_login_functionality(chrome_browser):

    # Test the login functionality of the Practice Test Automation website

    url = "https://practicetestautomation.com/practice-test-login/"

    # Navigate to login page
    chrome_browser.get(url)

    # Find and fill the username and password
    chrome_browser.find_element(By.ID,"username").send_keys("student")
    chrome_browser.find_element(By.ID,"password").send_keys("Password123")

    # Find and click on the submit button
    chrome_browser.find_element(By.ID,"submit").click()

    # Verify that the login was successful by checking the presence
    #  of a logout button

    try:  
        logout_button = chrome_browser.find_element(  
            By.CLASS_NAME, "wp-block-button__link"  
        )  
        assert logout_button.is_displayed(), "Logout button is not displayed."  
    except NoSuchElementException:  
        assert False, "Logout button does not exist."




        







