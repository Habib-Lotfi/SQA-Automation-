import unittest
from Pages.Login import Login
from Pages.MainPage import MainPage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_valid_login(self):
        self.driver.get(base_url)

        login = Login(self.driver)
        mainPage = MainPage(self.driver)

        login.enter_username("admin")
        login.enter_password("admin123")
        login.click_on_login_button()
        mainPage.check_main_page()

        # assert

        sleep(3)
        # Example assertion to check if the dashboard is displayed
        self.assertTrue(
            mainPage.check_main_page(), "Failed to log in or dashboard not found"
        )

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
            
if __name__ == "__main__":
    unittest.main()
