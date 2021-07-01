from selenium import webdriver

class Login:
    txtbox_username_id = "Email"
    txtbox_password_id = "Password"
    button_login_class = '//button[@class="button-1 login-button"]'
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, userName):
        self.driver.find_element_by_id(self.txtbox_username_id).clear()
        self.driver.find_element_by_id(self.txtbox_username_id).send_keys(userName)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.txtbox_password_id).clear()
        self.driver.find_element_by_id(self.txtbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_class).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()