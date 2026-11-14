from selenium.webdriver.common.by import By


class LoginPageLocators:
    FORGOT_PASSWORD_LINK = (
        By.CSS_SELECTOR,
        'a[href="/forgot-password"]',
    )

    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="Пароль"]')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    TITLE = (By.XPATH, '//h2[text()="Вход"]')