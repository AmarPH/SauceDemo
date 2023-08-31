import time

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig


class Test_Login:
    baseurl = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

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


