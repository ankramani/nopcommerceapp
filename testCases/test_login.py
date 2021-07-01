import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login

class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/admin/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = Login(self.driver)
        self.login.setUsername(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
        self.driver.close()