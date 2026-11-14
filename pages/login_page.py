import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Нажать «Восстановить пароль»')
    def click_forgot_password(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step('Войти в аккаунт')
    def login(self, email, password):
        self.fill(LoginPageLocators.EMAIL_INPUT, email)
        self.fill(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Получить заголовок страницы входа')
    def get_title(self):
        return self.get_text(LoginPageLocators.TITLE)