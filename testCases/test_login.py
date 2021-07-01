import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login

class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/admin/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self, setup):
        self.driver = setup