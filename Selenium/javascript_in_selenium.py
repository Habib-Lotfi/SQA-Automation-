from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

# to save a screenshot in an arbitrary path
from pathlib import Path
import os

#  To be as incognito in the browser
firefox_options = Options()
firefox_options.add_argument("--incognito")

# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install(),options=firefox_options))

driver.get("https://www.yahoo.com")
sleep(2)

# Scrolling current page to the maximum height of the page in the infinity page like "Yahoo"
# which applied lazy loading method
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
sleep(5)

# current Path(child) -> parent -> parent...
current_path = Path(__file__).parent

# convert the path to valid path for all OS systems
file_name = os.path.join(str(current_path), "NewScreenShot.png")


driver.save_screenshot(file_name)
driver.quit()
