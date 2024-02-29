import unittest
from Pages.Login import Login
from Pages.MainPage import MainPage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep




driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(base_url)
driver.implicitly_wait(3)

login = Login(driver)
mainPage = MainPage(driver)

login.enter_username("admin")
login.enter_password("admin123")
login.click_on_login_button()

mainPage.check_main_page()

# assert

sleep(3)
driver.quit()