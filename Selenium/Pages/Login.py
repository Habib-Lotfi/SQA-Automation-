from Locators import *


class Login:
    def __init__(self, driver):
        self.driver = driver
        # self.username_textbox_name = username_textbox_name
        # self.password_textbox_name = password_textbox_name
        # self.login_button_type = login_button_type

    def enter_username(self, username):
        # self.driver.find_element("name", self.username_textbox_name).send_keys(username)
        self.driver.find_element("name", username_textbox_name).send_keys(username)

    def enter_password(self, password):
        # self.driver.find_element("name", self.password_textbox_name).send_keys(password)
        self.driver.find_element("name", password_textbox_name).send_keys(password)

    def click_on_login_button(self):
        # self.driver.find_element("", self.login_textbox_type).click()
        self.driver.find_element(
            # "xpath", f"//button[@type='{self.login_button_type}']"
            "xpath",
            f"//button[@type='{login_button_type}']",
        ).click()
