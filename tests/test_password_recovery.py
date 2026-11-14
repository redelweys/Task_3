import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from urls import LOGIN_URL

from pages.reset_password_page import ResetPasswordPage
from urls import FORGOT_PASSWORD_URL


class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля')
    def test_forgot_password_link_opens_recovery_page(self, driver):
        login_page = LoginPage(driver)
        recovery_page = ForgotPasswordPage(driver)

        login_page.open(LOGIN_URL)
        login_page.click_forgot_password()

        assert recovery_page.get_title() == 'Восстановление пароля'

    @allure.title('Отправка почты открывает форму сброса пароля')
    def test_restore_password_opens_reset_form(
        self, driver, registered_user
    ):
        recovery_page = ForgotPasswordPage(driver)
        reset_page = ResetPasswordPage(driver)

        recovery_page.open(FORGOT_PASSWORD_URL)
        recovery_page.restore_password(registered_user['email'])

        assert reset_page.get_save_button_text() == 'Сохранить'

    @allure.title('Нажатие на глаз подсвечивает поле пароля')
    def test_password_visibility_click_activates_field(
        self, driver, registered_user
    ):
        recovery_page = ForgotPasswordPage(driver)
        reset_page = ResetPasswordPage(driver)

        recovery_page.open(FORGOT_PASSWORD_URL)
        recovery_page.restore_password(registered_user['email'])
        reset_page.click_password_visibility()

        assert reset_page.is_password_field_active()