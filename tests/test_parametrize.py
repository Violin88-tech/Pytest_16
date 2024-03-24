"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have

@pytest.fixture(params=[(1920, 1080), (1600, 900), (400, 800), (414, 896)])
def browser_manager(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.mark.desktop
@pytest.mark.parametrize('browser_manager', [(1680, 1050)], indirect=True)
def test_github_desktop(browser_manager):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').should(have.text('Sign in')).click()


@pytest.mark.mobile
@pytest.mark.parametrize('browser_manager', [(540, 960)], indirect=True)
def test_github_mobile(browser_manager):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').should(have.text('Sign in')).click()

