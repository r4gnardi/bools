

class Goods:

    def __init__(self, app):
        self.app = app

    def buy_first_goods(self):
        wd = self.app.wd
        wd.find_element_by_xpath('id("search-results")//img[@src = "https://uae.microless.com/cdn/products/22423-sm.jpg"]').click()
