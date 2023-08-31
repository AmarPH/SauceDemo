from selenium.webdriver.common.by import By


class Cart:

    Drop_Xpath = (By.XPATH, "//select[@class='product_sort_container']")
    Add_Jacket_Id = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    Add_BackPack_Id = (By.ID, "add-to-cart-sauce-labs-backpack")
    Add_TShirt_Id = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    Check_Cart_Xpath = (By.XPATH, "//a[@class='shopping_cart_link']")

    def __init__(self, driver):
        self.driver = driver

    def Add_Jacket(self):
        self.driver.find_element(*Cart.Add_Jacket_Id).click()

    def Add_BackPack(self):
        self.driver.find_element(*Cart.Add_BackPack_Id).click()

    def Add_TShirt(self):
        self.driver.find_element(*Cart.Add_TShirt_Id).click()

    def Check_Cart(self):
        self.driver.find_element(*Cart.Check_Cart_Xpath).click()
