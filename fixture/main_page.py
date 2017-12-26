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
        submenu = wd.find_element_by_xpath("//div[@id = 'menu-wrapper']//a[text() = 'Software'][@href ='https://uae.microless.com/software/']")
        ActionChains(wd).move_to_element(submenu).perform()
        wd.find_element_by_xpath('//div[@id = "menu-wrapper"]//a[text() = "Graphic Design"]').click()

    def open_home_page(self):
        wd = self.app.wd
        wd.get("https://uae.microless.com/")

    def open_product(self, product_name):
        wd = self.app.wd
        wd.find_element_by_id("query-desktop").send_keys(product_name)
        wd.find_element_by_xpath('//div[@class = "search-auto-complete-text"][text()="CorelDRAW Graphics Suite X7 - 1 User"]')


