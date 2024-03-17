import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    browser.config.base_url = 'https://github.com'

@pytest.fixture(params=[(1920, 1080), (1600, 900)])
def desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield

    browser.quit()

@pytest.fixture(params=[(800, 400), (896, 414)])
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


