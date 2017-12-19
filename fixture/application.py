from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.main_page import  MainPage
from fixture.goods import Goods

class Application:

    def __init__(self):
        self.wd = WebDriver("/home/ivn/Downloads/chromedriver")
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.main = MainPage(self)
        self.goods = Goods(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://uae.microless.com/")

    def destroy(self):
        self.wd.quit()

        ####

