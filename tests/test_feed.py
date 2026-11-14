import allure
import pytest

from pages.feed_page import FeedPage
from urls import FEED_URL

from pages.account_page import AccountPage

from pages.constructor_page import ConstructorPage
from urls import BASE_URL


class TestFeed:

    @allure.title('Клик по заказу открывает его детали')
    def test_order_click_opens_matching_details(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open(FEED_URL)

        expected_number = feed_page.open_first_order()

        assert feed_page.get_opened_order_number() == expected_number

    @allure.title('Заказ из истории пользователя отображается в ленте')
    def test_user_order_appears_in_history_and_feed(self, user_with_order):
        driver = user_with_order['driver']
        number = user_with_order['order_number']
        account_page = AccountPage(driver)
        feed_page = FeedPage(driver)

        account_page.click_account()
        account_page.click_order_history()
        found_in_history = account_page.has_order_in_history(number)

        feed_page.open(FEED_URL)

        assert found_in_history
        assert feed_page.has_order(number)

    @allure.title('После создания заказа растёт счётчик выполненных заказов')
    @pytest.mark.parametrize('counter', ['total', 'today'])
    def test_new_order_increases_completed_counter(
        self, logged_in_driver, counter
    ):
        feed_page = FeedPage(logged_in_driver)
        constructor_page = ConstructorPage(logged_in_driver)

        feed_page.open(FEED_URL)
        initial_count = feed_page.get_completed_count(counter)

        constructor_page.open(BASE_URL)
        constructor_page.add_bun()
        constructor_page.wait_for_bun_added()
        constructor_page.add_sauce()
        constructor_page.wait_for_sauce_counter(1)
        constructor_page.place_order()
        order_number = constructor_page.get_order_number()
        constructor_page.close_order()

        feed_page.open(FEED_URL)

        assert feed_page.has_order(order_number)
        assert feed_page.wait_for_completed_count_increase(
            counter, initial_count
        )

    @allure.title('Номер нового заказа появляется в разделе «В работе»')
    def test_new_order_number_appears_in_progress(self, logged_in_driver):
        constructor_page = ConstructorPage(logged_in_driver)
        feed_page = FeedPage(logged_in_driver)

        constructor_tab = constructor_page.get_current_tab()
        feed_tab = feed_page.open_new_tab(FEED_URL)
        feed_page.start_tracking_in_progress()

        constructor_page.switch_to_tab(constructor_tab)
        constructor_page.add_bun()
        constructor_page.wait_for_bun_added()
        constructor_page.add_sauce()
        constructor_page.wait_for_sauce_counter(1)
        constructor_page.place_order()
        order_number = constructor_page.get_order_number()

        feed_page.switch_to_tab(feed_tab)

        assert feed_page.was_order_in_progress(order_number)