# from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

base_url = "https://play1.automationcamp.ir/"
# ///////////////////////////////////
driver = webdriver.Firefox()
# driver.get("http://google.com")
# result_Search = driver.find_element('name','q')
# result_Search.send_keys("ancle Bob, clean code")
# result_Search.send_keys(Keys.RETURN)
# print(driver.title)
# driver.quit()
# //////////////////////////////////
driver.get(f"{base_url}/forms.html")
driver.find_element("id", "check_python").click()
check1 = driver.find_element("id", "check_validate").text
try:
    assert check1 == "PYTHON"
    print("check1::: OK")
except AssertionError:
    print("Assertion check1 failed")

text1 = "Hello automation World!"
driver.find_element("id", "notes").send_keys(text1)
check2 = driver.find_element("id", "area_notes_validate").text
try:
    assert check2 == text1
    print("check2::: OK")
except AssertionError:
    print("Assertion check2 failed")
