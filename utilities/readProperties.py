import configparser

config = configparser.RawConfigParser()
config.read("D:\\Credence Lect Videos\\Python\\Pytest\\Sauce_Demo\\Configuration\\Config.ini")


class ReadConfig:

    @staticmethod
    def getURL():
        url = config.get("common info", "baseurl")
        return url

    @staticmethod
    def getUsername():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password

    @staticmethod
    def getFirstname():
        firstname = config.get("checkout info", "firstname")
        return firstname

    @staticmethod
    def getLastname():
        lastname = config.get("checkout info", "lastname")
        return lastname

    @staticmethod
    def getPostalcode():
        postalcode = config.get("checkout info", "postalcode")
        return postalcode
