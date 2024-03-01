from Locators import dashboard_class


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        # self.dashboard_class = dashboard_class

    def check_main_page(self):
        # self.driver.find_element("class name",self.dashboard_class)
        element = self.driver.find_element("class name", dashboard_class)
        return element.is_displayed()
