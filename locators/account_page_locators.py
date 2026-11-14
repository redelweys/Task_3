from selenium.webdriver.common.by import By


class AccountPageLocators:
    ACCOUNT_LINK = (By.CSS_SELECTOR, 'a[href="/account"]')
    PROFILE_DESCRIPTION = (
        By.XPATH,
        '//*[text()="В этом разделе вы можете изменить '
        'свои персональные данные"]',
    )
    ORDER_HISTORY_LINK = (
        By.CSS_SELECTOR,
        'a[href="/account/order-history"]',
    )
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')

    OVERLAY = (
        By.CSS_SELECTOR,
        'div.Modal_modal_overlay__x2ZCr',
    )

    HISTORY_ORDER_NUMBER = (
        '//a[starts-with(@href, "/account/order-history/")]'
        '//p[starts-with(normalize-space(), "#")]'
        '[number(substring-after(normalize-space(), "#")) = {number}]'
    )