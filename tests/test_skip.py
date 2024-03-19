"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have

@pytest.fixture(params=[(1920, 1080), (1600, 900), (400, 800), (414, 896)])
def browser_manager(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height




@pytest.mark.desktop
def test_github_desktop(desktop_browser):
    if browser.config.window_width <= 600:
        pytest.skip('соотношение сторон десктопное')
    else:
        browser.open('/')
        browser.element('.HeaderMenu-link--sign-in').should(have.text('Sign in')).click()




@pytest.mark.mobile
def test_github_mobile(mobile_browser):
     if browser.config.window_width <= 600:
         pytest.skip('соотношение сторон мобильное')
     else:
         browser.open('/')
         browser.element('.Button--link').click()
         browser.element('.HeaderMenu-link--sign-in').should(have.text('Sign in')).click()





