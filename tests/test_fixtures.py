"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, have

@pytest.mark.desktop
def test_github_desktop():
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').should(have.text('Sign in')).click()

