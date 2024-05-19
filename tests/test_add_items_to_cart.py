from selene import browser, have
import requests
import allure
from allure_commons._allure import step
from allure_commons.types import AttachmentType

URL = 'https://demowebshop.tricentis.com/addproducttocart/catalog/'


def test_add_book_to_chart(open_browser):
    with step("Add book to shopping chart with API"):
        response = requests.post(url=f'{URL}13/1/1')
        allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    with step("Get cookie from API"):
        cookie = response.cookies.get('Nop.customer')

    with step("Set cookie from API"):
        browser.open('/cart')
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})
        browser.open('/cart')

    with step("Verify book in shopping cart"):
        browser.element('.product-name').should(have.text('Computing and Internet'))


def test_add_smartphone_to_chart(open_browser):
    with step("Add smartphone to shopping chart with API"):
        response = requests.post(url=f'{URL}43/1/1')
        allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    with step("Get cookie from API"):
        cookie = response.cookies.get('Nop.customer')

    with step("Set cookie from API"):
        browser.open('/cart')
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})
        browser.open('/cart')

    with step("Verify smartphone in shopping cart"):
        browser.element('.product-name').should(have.text('Smartphone'))


def test_add_jeans_to_chart(open_browser):
    with step("Add jeans to shopping chart with API"):
        response = requests.post(url=f'{URL}36/1/1')
        allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    with step("Get cookie from API"):
        cookie = response.cookies.get('Nop.customer')

    with step("Set cookie from API"):
        browser.open('/cart')
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})
        browser.open('/cart')

    with step("Verify jeans in shopping cart"):
        browser.element('.product-name').should(have.text('Blue Jeans'))
