import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage

from selenium.webdriver.common.by import By


class FeedPage(BasePage):

    @allure.step('Открыть первый заказ и запомнить его номер')
    def open_first_order(self):
        order = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(FeedPageLocators.FIRST_ORDER)
        )
        order_text = order.text
        order_href = order.get_attribute('href')
        order_number = int(order_text.splitlines()[0].lstrip('#'))

        relative_href = '/feed/' + order_href.rstrip('/').split('/')[-1]
        locator = (
            By.XPATH,
            FeedPageLocators.ORDER_BY_HREF.format(href=relative_href),
        )

        self.click_when_uncovered(locator, FeedPageLocators.OVERLAY)

        return order_number

    @allure.step('Получить номер заказа в открытом окне')
    def get_opened_order_number(self):
        text = self.get_text(FeedPageLocators.OPENED_ORDER_NUMBER)
        return int(text.strip().lstrip('#'))

    @allure.step('Проверить наличие заказа в общей ленте')
    def has_order(self, number):
        locator = (
            By.XPATH,
            FeedPageLocators.ORDER_NUMBER.format(number=int(number)),
        )
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()

    def get_counter_locator(self, counter):
        locators = {
            'total': FeedPageLocators.TOTAL_COMPLETED,
            'today': FeedPageLocators.TODAY_COMPLETED,
        }
        return locators[counter]

    @allure.step('Получить значение счётчика выполненных заказов')
    def get_completed_count(self, counter):
        locator = self.get_counter_locator(counter)
        return int(self.get_text(locator))

    @allure.step('Дождаться увеличения счётчика выполненных заказов')
    def wait_for_completed_count_increase(self, counter, initial):
        locator = self.get_counter_locator(counter)

        return WebDriverWait(self.driver, 30).until(
            lambda driver: int(driver.find_element(*locator).text) > initial
        )

    @allure.step('Начать наблюдение за номерами заказов в работе')
    def start_tracking_in_progress(self):
        container = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                FeedPageLocators.IN_PROGRESS_LIST
            )
        )

        self.driver.execute_script("""
            const container = arguments[0];

            if (window.inProgressObserver) {
                window.inProgressObserver.disconnect();
            }

            window.seenInProgress = [];

            function collect() {
                for (const item of container.querySelectorAll('li')) {
                    const text = item.textContent.trim();
                    if (/^\\d+$/.test(text)) {
                        const number = Number(text);
                        if (!window.seenInProgress.includes(number)) {
                            window.seenInProgress.push(number);
                        }
                    }
                }
            }

            window.inProgressObserver = new MutationObserver(collect);
            window.inProgressObserver.observe(container, {
                childList: true,
                subtree: true,
                characterData: true
            });

            collect();
        """, container)

    @allure.step('Проверить, что номер появился в разделе «В работе»')
    def was_order_in_progress(self, number):
        return WebDriverWait(self.driver, 30).until(
            lambda driver: driver.execute_script(
                'return (window.seenInProgress || []).includes(arguments[0]);',
                int(number),
            )
        )