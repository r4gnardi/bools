import pytest

from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_group(app):
    app.login(username="r4gnardi@gmail.com", password="xnj,znfr;bk")
    app.open_menu_subitem()
    app.logout()

def test_test_add_group1(app):
    app.login(username="r4gnardi@gmail.com", password="xnj,znfr;bk")


