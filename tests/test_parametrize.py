"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have


@pytest.mark.desktop
@pytest.mark.parametrize('desktop_browser', [(1680, 1050)], indirect=True)
def test_github_desktop(desktop_browser):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').should(have.text('Sign in')).click()


@pytest.mark.mobile
@pytest.mark.parametrize('mobile_browser', [(540, 960)], indirect=True)
def test_github_mobile(mobile_browser):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').should(have.text('Sign in')).click()

