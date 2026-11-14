import pytest
from selenium import webdriver

import random

import requests

from urls import REGISTER_URL, USER_URL, BASE_URL, LOGIN_URL

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage

from pages.constructor_page import ConstructorPage

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        browser = webdriver.Chrome()
    else:
        options = webdriver.FirefoxOptions()
        browser = webdriver.Firefox(options=options)

    try:
        browser.maximize_window()
        yield browser
    finally:
        browser.quit()

@pytest.fixture
def registered_user():
    suffix = random.randint(100000000000, 999999999999)
    user_data = {
        'email': f'qa_student_{suffix}@example.com',
        'password': 'TestPassword123!',
        'name': 'Test User',
    }

    response = requests.post(
        REGISTER_URL,
        json=user_data,
        timeout=30,
    )
    body = response.json()
    token = body.get('accessToken')

    try:
        assert response.status_code == 200
        assert body['success'] is True
        assert token

        yield user_data
    finally:
        if token:
            delete_response = requests.delete(
                USER_URL,
                headers={'Authorization': token},
                timeout=30,
            )
            delete_response.raise_for_status()
            assert delete_response.json()['success'] is True

@pytest.fixture
def logged_in_driver(driver, registered_user):
    login_page = LoginPage(driver)
    login_page.open(LOGIN_URL)
    login_page.login(
        registered_user['email'],
        registered_user['password'],
    )
    WebDriverWait(driver, 10).until(
        EC.url_to_be(f'{BASE_URL}/')
    )

    return driver

@pytest.fixture
def user_with_order(logged_in_driver):
    constructor_page = ConstructorPage(logged_in_driver)
    constructor_page.add_bun()
    constructor_page.wait_for_bun_added()
    constructor_page.add_sauce()
    constructor_page.wait_for_sauce_counter(1)
    constructor_page.place_order()

    order_number = constructor_page.get_order_number()
    constructor_page.close_order()

    return {
        'driver': logged_in_driver,
        'order_number': order_number,
    }