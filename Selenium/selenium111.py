from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# from selenium.webdriver.chrome.service import Service as ChromiumService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.os_manager import ChromeType

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

# base_url = "https://play1.automationcamp.ir/"
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# ///////////////////////////////////
# driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

# ###driver = webdriver.Firefox()// old method of executing firefox!
#  each system has a different driver, so driver manager will handle the suitable version
# Browser action -> open the web address (web page)
# driver.get("http://google.com")

#
# result_Search = driver.find_element('name','q')
# result_Search.send_keys("ancle Bob, clean code")
# result_Search.send_keys(Keys.RETURN)
# print(driver.title)
# driver.quit()
# //////////////////////////////////

# Browser action 1 -> open the web address (web page)
# driver.get(f"{base_url}/forms.html")

# Browser action 2 -> Fetch the page title
# page_title = driver.title
# print(page_title)

#  Browser action 3 -> Back key (to the pervious page)
#  Brows new page
driver.get("http://google.com")
# page_title = driver.title
# print(page_title)
# sleep(2)

# Back to pervious page
# driver.back()
# page_title = driver.title
# print(page_title)
# sleep(2)

# Browser action 4 -> Forward key
# driver.forward()

# Browser action 5 -> Refresh the page
# driver.refresh()

# Browser action 6 -> Open a new tab and switch to it (as active window)
driver.switch_to.new_window("tab")
# page_title = driver.title  # value of it is null (blank). It is same for new window
# print(page_title)
# sleep(2)

# Browser action 7 -> Open the browser window and switch to it (as active window)
# driver.switch_to.new_window("window")
# driver.get("https://gmail.com")
# page_title = driver.title
# print(page_title)
# sleep(2)

# # Browser action 8 -> Current Window
# gmail_window = driver.current_window_handle
# print("gmail window handler = " + str(gmail_window))

# Browser action 9 -> All windows handle
# all_windows_handler = driver.window_handles
# print("All window handler = " + str(all_windows_handler))

# Browser action 10 -> Switch between windows
# driver.switch_to.window(all_windows_handler[1])
# sleep(2)
# # Browser action 11 -> Closing current window (tab)
# print("CLosinggggggggggggggggggg")
# driver.close()
# sleep(5)

# driver.find_element("id", "check_python").click()
# check1 = driver.find_element("id", "check_validate").text
# sleep(2)
# try:
#     assert check1 == "PYTHON"
#     print("check1::: OK")
# except AssertionError:
#     print("Assertion check1 failed")

# text1 = "Hello automation World!"
# driver.find_element("id", "notes").send_keys(text1)
# check2 = driver.find_element("id", "area_notes_validate").text
# sleep(3)

# try:
#     assert check2 == text1
#     print("check2::: OK")
# except AssertionError:
#     print("Assertion check2 failed")

# Browser action 12 -> Close sessions (close all browser sessions [Software (FireFox)])
# driver.quit()

# Browser action 13 -> Window size
# print(driver.get_window_size())

window_size = driver.get_window_size()
# print("old window size:  ",window_size)
# window_height = window_size['height']
# window_width = window_size['width']
# print(window_height,"   ",window_width)

# Browser action 14 ->Set Window Size (resize window)
driver.set_window_size(800, 600)
new_window_size = driver.get_window_size()
# print("new window size:  ", new_window_size)

# Browser action 15 -> Get window position
window_position = driver.get_window_position()
print("new window position: ", window_position)
# sleep(3)

# Browser action 16 -> Change window position
driver.set_window_position(20, 50)

# Browser action 17 -> Maximize window
driver.maximize_window()
sleep(3)

# Browser action 18 -> Minimize window
driver.minimize_window()
sleep(3)

# Browser action 19 -> Fullscerene window
driver.fullscreen_window()

sleep(3)


driver.quit()
