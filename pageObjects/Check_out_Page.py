from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Checkout:
    Click_Checkout_Id = (By.ID, "checkout")
    Firstname_Box_Id = (By.ID, "first-name")
    Lastname_Box_Id = (By.ID, "last-name")
    Postal_Code_Id = (By.ID, "postal-code")
    Continue_Button_Id = (By.ID, "continue")
    Item_total_Xpath = (By.XPATH, "//div[@class='summary_subtotal_label']")
    Item_Tax_Xpath = (By.XPATH, "//div[@class='summary_tax_label']")
    Total_Cost_Xpath = (By.XPATH, "//div[@class='summary_info_label summary_total_label']")
    Finish_Button_Id = (By.ID, "finish")
    Order_Xpath = (By.XPATH, "//h2[normalize-space()='Thank you for your order!']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def Click_Checkout(self):
        self.driver.find_element(*Checkout.Click_Checkout_Id).click()

    def Firstname_Box(self, firstname):
        self.driver.find_element(*Checkout.Firstname_Box_Id).send_keys(firstname)

    def Lastname_Box(self, lastname):
        self.driver.find_element(*Checkout.Lastname_Box_Id).send_keys(lastname)

    def Postal_Code(self, postalcode):
        self.driver.find_element(*Checkout.Postal_Code_Id).send_keys(postalcode)

    def Continue_Button(self):
        self.driver.find_element(*Checkout.Continue_Button_Id).click()

    def Item_total(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Item_total_Xpath))
        print(self.driver.find_element(*Checkout.Item_total_Xpath).text)

    def Item_tax(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Item_Tax_Xpath))
        print(self.driver.find_element(*Checkout.Item_Tax_Xpath).text)

    def Total_Cost(self):
        print(self.driver.find_element(*Checkout.Total_Cost_Xpath).text)

    def Finish_Button(self):
        self.driver.find_element(*Checkout.Finish_Button_Id).click()

    def Order_placed(self):
        print(self.driver.find_element(*Checkout.Order_Xpath).text)
