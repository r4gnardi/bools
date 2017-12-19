from selenium.webdriver import ActionChains


class MainPage:
    def __init__(self, app):
        self.app = app

    def top(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('img[src="https://uae.microless.com/cdn/brands/hp.png"]').click()
        wd.find_elements_by_css_selector('div[data-listid = "search"]')

    def open_menu_subitem(self):
        wd = self.app.wd
        main_menu = wd.find_element_by_id("menu-toggle")
        ActionChains(wd).move_to_element(main_menu).perform()
        submenu = wd.find_element_by_xpath('id("menu-wrapper")/ul[1]/li[5]/a[1]')
        ActionChains(wd).move_to_element(submenu).perform()
        wd.find_element_by_xpath('id("menu-wrapper")/ul[1]/li[5]/div[1]/div[1]/ul[1]/li[4]/a[1]').click()

