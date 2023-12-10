import os

import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import browser
from selene.support.conditions import have
import allure
import json
import logging
from time import sleep



LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
WEB_URL = "https://demowebshop.tricentis.com/"
API_URL = "https://demowebshop.tricentis.com/"


def test_login_through_api(browser_setup):
    with step("Login with API"):
        result = requests.post(
            url=API_URL + "/login",
            data={"Email": LOGIN, "Password": PASSWORD, "RememberMe": False},
            allow_redirects=False
        )
        assert result.status_code == 302
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)


    global cookie
    with step("Get cookie from API"):
        cookie = result.cookies.get("NOPCOMMERCE.AUTH")

    with step("Set cookie from API and open web url"):
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open(WEB_URL)

    with step("Verify successful authorization"):
        browser.element('.account').should(have.text(f'{LOGIN}'))




def test_add_laptop_to_cart(browser_setup):
    with step("Adding to cart a lapton"):
        result = requests.post(
            url=API_URL + '/addproducttocart/details/31/1',
            data={'addtocart_31.EnteredQuantity': 1},
            cookies={"NOPCOMMERCE.AUTH": cookie}
        )
        assert result.status_code == 200
        # allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response", attachment_type=AttachmentType.JSON, extension="json")
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)


    with step("Set cookie from API and open web url"):
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open(WEB_URL)
        browser.element('#topcartlink > a > span.cart-label').click()

    with step('Checking cart for added latop'):
            browser.element('.cart').should(have.text('14.1-inch Laptop'))



def test_add_smartphone_to_cart(browser_setup):
    with step("Adding to cart a smartphone"):
        result = requests.post(
            url=API_URL + '/addproducttocart/details/43/1',
            data={'addtocart_43.EnteredQuantity': 1},
            cookies={"NOPCOMMERCE.AUTH": cookie}
        )
        assert result.status_code == 200
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response", attachment_type=AttachmentType.JSON, extension="json")
        # allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)


    with step("Set cookie from API and open web url"):
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open(WEB_URL)
        browser.element('#topcartlink > a > span.cart-label').click()

    with step('Checking cart for added smartphone'):
        browser.element('.cart').should(have.text('Smartphone'))


def test_add_book_to_cart(browser_setup):
    with step("Adding to cart a book"):
        result = requests.post(
            url=API_URL + '/addproducttocart/details/22/1',
            data={'addtocart_22.EnteredQuantity': 1},
            cookies={"NOPCOMMERCE.AUTH": cookie}
        )
        assert result.status_code == 200
        # allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response", attachment_type=AttachmentType.JSON, extension="json")
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)


    with step("Set cookie from API and open web url"):
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open(WEB_URL)
        browser.element('#topcartlink > a > span.cart-label').click()

    with step('Checking cart for added book'):
        browser.element('.cart').should(have.text('Health Book'))


