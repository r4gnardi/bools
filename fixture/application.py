from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import ActionChains


class Application:

    def __init__(self):
        self.wd = WebDriver("/home/ivn/Downloads/chromedriver")
        self.wd.implicitly_wait(60)

    def logout(self):
        wd = self.wd
        #logout = wd.find_element_by_css_selector('a[href = "http://uae.microless.com/login/"][class="button-link"]')
        logout = wd.find_element_by_xpath('//ancestor::span[text()="Your Account"]')
        ActionChains(wd).move_to_element(logout).perform()
        wd.find_element_by_link_text("Log Out").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_link_text("Your Account").click()
        wd.find_element_by_id("email").click()
        wd.find_element_by_id("email").clear()
        wd.find_element_by_id("email").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath('//button[text() = "Log in"]').click()

    def open_menu_subitem(self):
        wd = self.wd
        main_menu = wd.find_element_by_id("menu-toggle")
        ActionChains(wd).move_to_element(main_menu).perform()
        submenu = wd.find_element_by_xpath('id("menu-wrapper")/ul[1]/li[5]/a[1]')
        ActionChains(wd).move_to_element(submenu).perform()
        wd.find_element_by_xpath('id("menu-wrapper")/ul[1]/li[5]/div[1]/div[1]/ul[1]/li[4]/a[1]').click()

    def open_home_page(self):
        wd = self.wd
        wd.get("https://uae.microless.com/")

    def destroy(self):
        self.wd.quit()

        ####

