from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:

    Username_box_ID = (By.ID, "user-name")
    Password_box_ID = (By.ID, "password")
    Login_button_ID = (By.ID, "login-button")
    Login_status_XPATH = (By.XPATH, "//div[@class='app_logo']")
    Filter_button_XPATH = (By.XPATH, "//select[@class='product_sort_container']")

    def __init__(self, driver):
        self.driver = driver

    def Username_box(self, username):
        self.driver.find_element(*Login.Username_box_ID).send_keys(username)

    def Password_box(self, password):
        self.driver.find_element(*Login.Password_box_ID).send_keys(password)

    def Login_button(self):
        self.driver.find_element(*Login.Login_button_ID).click()

    def Login_status(self):
        try:
            self.driver.find_element(*Login.Login_status_XPATH)
            return True
        except:
            return False
