# tests/pages/search_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchPage:

    # Method to build a constructor of this class
    def __init__(self, driver):
        self.driver = driver

    # Method which open a website
    def open_web_page(self,url):
        self.driver.get(url)

    # Method which find a search box and then 
    # put the expression words seraching

    def search_page(self,search_term):
        search_box = self.driver.find_element(By.ID,"searchbox_input")
        search_box.send_keys(search_term +Keys.RETURN)

    # Verify that a new page will open successful or not
    def verify_searching_page(self, search_term):
        assert search_term in self.driver.title

