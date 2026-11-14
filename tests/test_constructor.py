import allure

from pages.constructor_page import ConstructorPage
from urls import BASE_URL, FEED_URL, LOGIN_URL


class TestConstructor:

    @allure.title('Клик по ингредиенту открывает его детали')
    def test_ingredient_click_opens_details(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open(BASE_URL)

        constructor_page.open_bun_details()

        assert constructor_page.get_ingredient_details_title() == (
            'Детали ингредиента'
        )

    @allure.title('Крестик закрывает детали ингредиента')
    def test_close_button_closes_ingredient_details(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open(BASE_URL)
        constructor_page.open_bun_details()

        constructor_page.close_ingredient_details()

        assert constructor_page.is_ingredient_details_closed()

    @allure.title('Переход в конструктор по ссылке в меню')
    def test_constructor_link_opens_constructor(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open(LOGIN_URL)

        constructor_page.click_constructor()

        assert constructor_page.wait_for_url(f'{BASE_URL}/')
        assert constructor_page.get_title() == 'Соберите бургер'

    @allure.title('Переход в ленту заказов по ссылке в меню')
    def test_feed_link_opens_order_feed(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open(BASE_URL)

        constructor_page.click_feed()

        assert constructor_page.wait_for_url(FEED_URL)

    @allure.title('Добавление соуса увеличивает его счётчик на один')
    def test_add_ingredient_increases_counter(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open(BASE_URL)
        initial_counter = constructor_page.get_sauce_counter()

        constructor_page.add_sauce()

        assert constructor_page.wait_for_sauce_counter(
            initial_counter + 1
        )
        assert constructor_page.get_sauce_counter() == initial_counter + 1

    @allure.title('Авторизованный пользователь оформляет заказ')
    def test_logged_in_user_can_place_order(self, logged_in_driver):
        constructor_page = ConstructorPage(logged_in_driver)
        constructor_page.add_bun()
        constructor_page.wait_for_bun_added()
        constructor_page.add_sauce()
        constructor_page.wait_for_sauce_counter(1)

        constructor_page.place_order()

        assert constructor_page.get_order_number() > 0
        assert constructor_page.get_order_confirmation() == (
            'Ваш заказ начали готовить'
        )