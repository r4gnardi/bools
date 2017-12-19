from selenium.webdriver import ActionChains


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def logout(self):
        wd = self.app.wd
        logout = wd.find_element_by_css_selector('a[href = "http://uae.microless.com/account/"][class ="button-link"]')
        ActionChains(wd).move_to_element(logout).perform()
        wd.find_element_by_link_text("Log Out").click()

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_link_text("Your Account").click()
        wd.find_element_by_id("email").click()
        wd.find_element_by_id("email").clear()
        wd.find_element_by_id("email").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath('//button[text() = "Log in"]').click()