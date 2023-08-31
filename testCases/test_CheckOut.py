import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

from pageObjects.Check_out_Page import Checkout
from pageObjects.LoginPage import Login
from pageObjects.page_Add_To_Cart import Cart
from utilities.readProperties import ReadConfig


class Test_Login:
    baseurl = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    firstname = ReadConfig.getFirstname()
    lastname = ReadConfig.getLastname()
    postalcode = ReadConfig.getPostalcode()

    def test_Login_001(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.lp.Username_box(self.username)
        self.lp.Password_box(self.password)
        self.lp.Login_button()
        time.sleep(2)

        if self.driver.title == "Swag Labs":
            print("\n***** Login Passed *****")
            assert True
        else:
            assert False

        self.atc = Cart(self.driver)
        time.sleep(2)
        drp = Select(self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
        drp.select_by_index(3)

        self.atc.Add_Jacket()
        self.atc.Add_BackPack()
        self.atc.Add_TShirt()
        self.atc.Check_Cart()

        time.sleep(2)

        self.chkout = Checkout(self.driver)
        self.chkout.Click_Checkout()
        self.chkout.Firstname_Box(self.firstname)
        self.chkout.Lastname_Box(self.lastname)
        self.chkout.Postal_Code(self.postalcode)
        self.chkout.Continue_Button()
        cost1 = self.chkout.Item_total()
        cost2 = self.chkout.Item_tax()
        # final_cost = cost1 + cost2
        # print("Final Amount : ", final_cost)
        self.chkout.Total_Cost()
        self.chkout.Finish_Button()
        self.chkout.Order_placed()
