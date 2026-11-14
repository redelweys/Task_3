import allure

from pages.account_page import AccountPage
from pages.login_page import LoginPage
from urls import LOGIN_URL, ORDER_HISTORY_URL


class TestAccount:

    @allure.title('Переход в личный кабинет')
    def test_account_link_opens_profile(self, logged_in_driver):
        account_page = AccountPage(logged_in_driver)

        account_page.click_account()

        assert account_page.get_profile_description() == (
            'В этом разделе вы можете изменить '
            'свои персональные данные'
        )

    @allure.title('Переход в историю заказов')
    def test_order_history_link_opens_history(self, logged_in_driver):
        account_page = AccountPage(logged_in_driver)
        account_page.click_account()

        account_page.click_order_history()

        assert account_page.wait_for_url(ORDER_HISTORY_URL)

    @allure.title('Выход из аккаунта')
    def test_logout_opens_login_page(self, logged_in_driver):
        account_page = AccountPage(logged_in_driver)
        login_page = LoginPage(logged_in_driver)
        account_page.click_account()

        account_page.logout()

        assert login_page.wait_for_url(LOGIN_URL)
        assert login_page.get_title() == 'Вход'