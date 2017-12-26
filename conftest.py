import pytest

from fixture.application import Application


@pytest.fixture(scope="session", params={'chrome'})
def app(request):
    fixture = Application(request.param)
    request.addfinalizer(fixture.destroy)
    return fixture
