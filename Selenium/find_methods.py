from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
base_url = "https://www.wikipedia.org/"

driver.get(base_url)

# 1> ID
element1 = driver.find_element("id", "searchInput")
element1.send_keys("Hello World!")
sleep(2)

# 2> Xpath
# 2.1> Absolute path "/<Tag>/<Tag>/<Tag>..."  <<<Not working>>>
# element2_1 = driver.find_element("xpath", "/html/body/div[3]")
# element2_1 = driver.find_element("xpath", "/html/body/main/div[2]/form/fieldset/div/input//div")

# 2.2> Relative Xpath "//<Tag>[<attribute>='value']"
# element2 = driver.find_element("xpath","//input[@text(search)]")
# element2 = driver.find_element("xpath","//input[@name='search']")
# Applying the single quotes '' and double quotes "" are in reverse order same as examples above and below
# element2_2 = driver.find_element("xpath", '//input[@type="search"]')

# assert element1 == element2_2

# print("Element1: ", element1)
# # print("Element2_1: ", element2_1)
# print("Element2_2: ", element2_2)

# element3 = driver.find_element("xpath", "//*[text()='Italiano']")
# element3.click()
# sleep(3)

# 3> Tag
# element4 = driver.find_element("tag name", "select")
# element4.click()
# sleep(3)

# 4> Link Text
# element5 = driver.find_element("link text", "Download Wikipedia for Android or iOS")
# element5.click()
# sleep(3)

# 5> Partial Link Text
# element6 = driver.find_element("partial link text", "Download")
# element6.click()
# sleep(3)

# 6> Class Name
# element6 = driver.find_element("class name", "svg-search-icon")
# element6.click()
# sleep(3)

# 7> CSS Selector
# element7_1 = driver.find_element("css selector", ".svg-search-icon")#for finding a class
# element7_1.click()
# sleep(3)

element7_2 = driver.find_element("css selector", "#searchInput")#for finding an ID
element7_2.send_keys("That is GOOOOOOOOOD")
sleep(3)


driver.quit()
