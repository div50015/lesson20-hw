import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import browser
from selene.support.conditions import have
import allure

LOGIN = "example1200@example.com"
PASSWORD = "123456"
WEB_URL = "https://demowebshop.tricentis.com/"
API_URL = "https://demowebshop.tricentis.com/"


def test_login():
    browser.open("http://demowebshop.tricentis.com/login")

    browser.element("#Email").send_keys(LOGIN)
    browser.element("#Password").send_keys(PASSWORD).press_enter()

    browser.element(".account").should(have.text(LOGIN))
