import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage
from urls import PROFILE_URL


class AccountPage(BasePage):

    @allure.step('Открыть личный кабинет')
    def click_account(self):
        self.click_when_uncovered(
            AccountPageLocators.ACCOUNT_LINK,
            AccountPageLocators.OVERLAY,
        )
        self.wait_for_url(PROFILE_URL)

    @allure.step('Получить описание профиля')
    def get_profile_description(self):
        return self.get_text(AccountPageLocators.PROFILE_DESCRIPTION)

    @allure.step('Открыть историю заказов')
    def click_order_history(self):
        self.click_when_uncovered(
            AccountPageLocators.ORDER_HISTORY_LINK,
            AccountPageLocators.OVERLAY,
        )

    @allure.step('Выйти из аккаунта')
    def logout(self):
        self.click_when_uncovered(
            AccountPageLocators.LOGOUT_BUTTON,
            AccountPageLocators.OVERLAY,
        )

    @allure.step('Проверить наличие заказа в истории пользователя')
    def has_order_in_history(self, number):
        locator = (
            By.XPATH,
            AccountPageLocators.HISTORY_ORDER_NUMBER.format(
                number=int(number)
            ),
        )
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()