import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

from locators.constructor_page_locators import ConstructorPageLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):

    @allure.step('Открыть детали Краторной булки')
    def open_bun_details(self):
        self.click_when_uncovered(
            ConstructorPageLocators.BUN_CARD,
            ConstructorPageLocators.OVERLAY,
        )

    @allure.step('Получить заголовок окна ингредиента')
    def get_ingredient_details_title(self):
        return self.get_text(
            ConstructorPageLocators.INGREDIENT_DETAILS_TITLE
        )

    @allure.step('Закрыть детали ингредиента крестиком')
    def close_ingredient_details(self):
        self.click(ConstructorPageLocators.INGREDIENT_DETAILS_CLOSE)

    @allure.step('Проверить закрытие окна ингредиента')
    def is_ingredient_details_closed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(
                ConstructorPageLocators.INGREDIENT_DETAILS_TITLE
            )
        )

    @allure.step('Нажать «Конструктор»')
    def click_constructor(self):
        self.click_when_uncovered(
            ConstructorPageLocators.CONSTRUCTOR_LINK,
            ConstructorPageLocators.OVERLAY,
        )

    @allure.step('Нажать «Лента заказов»')
    def click_feed(self):
        self.click_when_uncovered(
            ConstructorPageLocators.FEED_LINK,
            ConstructorPageLocators.OVERLAY,
        )

    @allure.step('Получить заголовок конструктора')
    def get_title(self):
        return self.get_text(ConstructorPageLocators.TITLE)

    @allure.step('Получить значение счётчика соуса')
    def get_sauce_counter(self):
        return int(self.get_text(ConstructorPageLocators.SAUCE_COUNTER))

    @allure.step('Перетащить ингредиент в заказ')
    def add_ingredient(self, locator):
        self.wait_until_hidden(ConstructorPageLocators.OVERLAY)

        ingredient = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        
        target = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                ConstructorPageLocators.DROP_AREA
            )
        )

        if self.driver.capabilities['browserName'] == 'firefox':
            self.driver.execute_script("""
                const source = arguments[0];
                const target = arguments[1];
                const dataTransfer = new DataTransfer();

                function fire(element, type) {
                    element.dispatchEvent(new DragEvent(type, {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    }));
                }

                fire(source, 'dragstart');
                fire(target, 'dragenter');
                fire(target, 'dragover');
                fire(target, 'drop');
                fire(source, 'dragend');
            """, ingredient, target)
        else:
            ActionChains(self.driver).drag_and_drop(
                ingredient, target
            ).perform()

    @allure.step('Дождаться ожидаемого значения счётчика соуса')
    def wait_for_sauce_counter(self, expected):
        try:
            return WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(
                    *ConstructorPageLocators.SAUCE_COUNTER
                ).text == str(expected)
            )
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name='Конструктор после перетаскивания',
                attachment_type=allure.attachment_type.PNG,
            )
            actual = self.driver.find_element(
                *ConstructorPageLocators.SAUCE_COUNTER
            ).text
            basket = self.driver.find_element(
                *ConstructorPageLocators.DROP_AREA
            ).text

            raise TimeoutException(
                f'Ожидали счётчик {expected}, фактически: {actual!r}. '
                f'Содержимое области заказа: {basket!r}'
            ) from None

    @allure.step('Добавить соус')
    def add_sauce(self):
        self.add_ingredient(ConstructorPageLocators.SAUCE_CARD)

    @allure.step('Добавить булочку')
    def add_bun(self):
        self.add_ingredient(ConstructorPageLocators.BUN_CARD)

    @allure.step('Дождаться добавления двух половинок булочки')
    def wait_for_bun_added(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(
                *ConstructorPageLocators.BUN_COUNTER
            ).text == '2'
        )

    @allure.step('Оформить заказ')
    def place_order(self):
        self.click_when_uncovered(
            ConstructorPageLocators.ORDER_BUTTON,
            ConstructorPageLocators.OVERLAY,
        )

    @allure.step('Дождаться номера оформленного заказа')
    def get_order_number(self):
        def actual_number(driver):
            element = EC.visibility_of_element_located(
                ConstructorPageLocators.ORDER_NUMBER
            )(driver)
            if not element:
                return False

            number = element.text.strip()
            if number.isdigit() and int(number) > 0 and number != '9999':
                return int(number)

            return False

        return WebDriverWait(self.driver, 30).until(actual_number)

    @allure.step('Получить подтверждение оформления заказа')
    def get_order_confirmation(self):
        return self.get_text(ConstructorPageLocators.ORDER_CONFIRMATION)

    @allure.step('Закрыть окно оформленного заказа')
    def close_order(self):
        self.click_when_ready(ConstructorPageLocators.ORDER_CLOSE_BUTTON)
        self.wait_until_hidden(ConstructorPageLocators.ORDER_NUMBER)