import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

from pageObjects.LoginPage import Login
from pageObjects.page_Add_To_Cart import Cart


class Test_Login:

    def test_Login_001(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.Username_box("standard_user")
        self.lp.Password_box("secret_sauce")
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

        time.sleep(5)


            


