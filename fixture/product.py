

class Product:

    def __init__(self, app):
        self.app = app

    def click_buy(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('button[data-prodid = "10312"]').click()

