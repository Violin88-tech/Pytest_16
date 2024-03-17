"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have



@pytest.mark.desktop
def test_github_desktop(desktop_browser):
    if not desktop_browser:
        pytest.skip('соотношение сторон десктопное')
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').should(have.text('Sign in')).click()


@pytest.mark.mobile
def test_github_mobile(mobile_browser):
     if not mobile_browser:
         pytest.skip('соотношение сторон мобильное')
     browser.open('/')
     browser.element('.Button--link').click()
     browser.element('.HeaderMenu-link--sign-in').should(have.text('Sign in')).click()




