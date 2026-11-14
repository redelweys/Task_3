import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('Получить заголовок страницы восстановления пароля')
    def get_title(self):
        return self.get_text(ForgotPasswordPageLocators.TITLE)

    @allure.step('Ввести почту и нажать «Восстановить»')
    def restore_password(self, email):
        self.fill(ForgotPasswordPageLocators.EMAIL_INPUT, email)
        self.click(ForgotPasswordPageLocators.RESTORE_BUTTON)