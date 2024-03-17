"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, have


def test_github_desktop(desktop_browser):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').should(have.text('Sign in')).click()


def test_github_main_page_mobile(mobile_browser):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').should(have.text('Sign in')).click()