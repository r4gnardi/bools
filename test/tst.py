def test_check_price_cd(app):
    app.session.login(username="r4gnardi@gmail.com", password="xnj,znfr;bk")
    app.main.open_menu_subitem()
    app.goods.buy_first_goods()
    price = app.wd.find_element_by_css_selector("span.product-price").text
    app.session.logout()
    assert price == "2,275.00"


def test_num_of_hp_products(app):
    app.open_home_page()
    app.main.top()
    num = app.wd.find_element_by_css_selector("div.search-result-summary").text
    assert "1670" in num



