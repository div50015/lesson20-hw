import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import browser
from selene.support.conditions import have
import allure
from time import sleep


LOGIN = "test@qa.guru.com"
PASSWORD = "123456"
# LOGIN = "example1200@example.com"
# PASSWORD = "123456"
WEB_URL = "https://demowebshop.tricentis.com/"
API_URL = "https://demowebshop.tricentis.com/"


def test_login_though_api():
    result = requests.post(
        url=API_URL + "/login",
        data={"Email": LOGIN, "Password": PASSWORD, "RememberMe": False},
        allow_redirects=False
    )
    assert result.status_code == 302
    cookie = result.cookies.get("NOPCOMMERCE.AUTH")

    result = requests.post(url=API_URL + '/addproducttocart/catalog/31/1/1')
    assert result.status_code == 200
    result = requests.post(url=API_URL + '/addproducttocart/details/75/1')
    assert result.status_code == 200
    result = requests.post(url=API_URL + "/addproducttocart/details/72/1")
    assert result.status_code == 200

    # cookie = result.cookies.get("NOPCOMMERCE.AUTH")

    browser.open(WEB_URL)
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    browser.open(WEB_URL)

    browser.element(".account").should(have.text(LOGIN))

    browser.element('#topcartlink > a > span.cart-label').click()
    sleep(10)

