from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    TITLE = (
        By.XPATH,
        '//h2[text()="Восстановление пароля"]',
    )

    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')
    RESTORE_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')