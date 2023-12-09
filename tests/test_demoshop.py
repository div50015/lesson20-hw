import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import browser
from selene.support.conditions import have
import allure
from time import sleep


# LOGIN = "test@qa.guru.com"
# PASSWORD = "123456"
LOGIN = "example1200@example.com"
PASSWORD = "123456"
WEB_URL = "https://demowebshop.tricentis.com/"
API_URL = "https://demowebshop.tricentis.com/"


def test_login_through_api():
    result = requests.post(
        url=API_URL + "/login",
        data={"Email": LOGIN, "Password": PASSWORD, "RememberMe": False},
        allow_redirects=False
    )
    assert result.status_code == 302

    global cookie
    cookie = result.cookies.get("NOPCOMMERCE.AUTH")

    browser.open(WEB_URL)
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    browser.open(WEB_URL)

    browser.element('.account').should(have.text('example1200@example.com'))




def test_add_laptop_to_cart():
    result = requests.post(url=API_URL + '/addproducttocart/details/31/1', data={'addtocart_31.EnteredQuantity': 1}, cookies={"NOPCOMMERCE.AUTH": cookie})
    assert result.status_code == 200

    browser.open(WEB_URL)
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    browser.open(WEB_URL)
    browser.element('#topcartlink > a > span.cart-label').click()

    browser.element('.cart').should(have.text('14.1-inch Laptop'))



def test_add_smartphone_to_cart():
    result = requests.post(url=API_URL + '/addproducttocart/details/43/1', data={'addtocart_43.EnteredQuantity': 1}, cookies={"NOPCOMMERCE.AUTH": cookie})
    assert result.status_code == 200

    browser.open(WEB_URL)
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    browser.open(WEB_URL)

    browser.element('#topcartlink > a > span.cart-label').click()

    browser.element('.cart').should(have.text('Smartphone'))


def test_add_book_to_cart():
    result = requests.post(url=API_URL + '/addproducttocart/details/22/1', data={'addtocart_22.EnteredQuantity': 1}, cookies={"NOPCOMMERCE.AUTH": cookie})
    assert result.status_code == 200

    browser.open(WEB_URL)
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    browser.open(WEB_URL)

    browser.element('#topcartlink > a > span.cart-label').click()

    browser.element('.cart').should(have.text('Health Book'))



