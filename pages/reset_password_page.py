import allure

from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ResetPasswordPage(BasePage):

    @allure.step('Получить текст кнопки сохранения нового пароля')
    def get_save_button_text(self):
        return self.get_text(ResetPasswordPageLocators.SAVE_BUTTON)

    @allure.step('Нажать на значок видимости пароля')
    def click_password_visibility(self):
        self.click_when_ready(
            ResetPasswordPageLocators.PASSWORD_VISIBILITY_ICON
        )

    @allure.step('Проверить подсветку поля пароля')
    def is_password_field_active(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                ResetPasswordPageLocators.ACTIVE_PASSWORD_FIELD
            )
        ).is_displayed()