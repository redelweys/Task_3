from selenium.webdriver.common.by import By


class ConstructorPageLocators:
    BUN_CARD = (
        By.XPATH,
        '//a[starts-with(@href, "/ingredient/")]'
        '[.//p[text()="Краторная булка N-200i"]]',
    )
    INGREDIENT_DETAILS_TITLE = (
        By.XPATH,
        '//h2[text()="Детали ингредиента"]',
    )
    INGREDIENT_DETAILS_CLOSE = (
        By.XPATH,
        '//h2[text()="Детали ингредиента"]'
        '/parent::div/parent::div//button',
    )
    OVERLAY = (
        By.CSS_SELECTOR,
        'div.Modal_modal_overlay__x2ZCr',
    )

    CONSTRUCTOR_LINK = (
        By.XPATH,
        '//a[@href="/"][.//p[text()="Конструктор"]]',
    )
    FEED_LINK = (By.CSS_SELECTOR, 'a[href="/feed"]')
    TITLE = (By.XPATH, '//h1[text()="Соберите бургер"]')

    SAUCE_CARD = (
        By.XPATH,
        '//a[starts-with(@href, "/ingredient/")]'
        '[.//p[text()="Соус Spicy-X"]]',
    )
    SAUCE_COUNTER = (
        By.XPATH,
        '//a[starts-with(@href, "/ingredient/")]'
        '[.//p[text()="Соус Spicy-X"]]'
        '//p[contains(@class, "counter_counter__num")]',
    )
    DROP_AREA = (
        By.CSS_SELECTOR,
        'section.BurgerConstructor_basket__29Cd7',
    )

    ORDER_BUTTON = (
        By.XPATH,
        '//button[text()="Оформить заказ"]',
    )
    ORDER_NUMBER = (
        By.XPATH,
        '//p[text()="идентификатор заказа"]'
        '/preceding-sibling::h2',
    )
    ORDER_CONFIRMATION = (
        By.XPATH,
        '//p[text()="Ваш заказ начали готовить"]',
    )
    BUN_COUNTER = (
        By.XPATH,
        '//a[starts-with(@href, "/ingredient/")]'
        '[.//p[text()="Краторная булка N-200i"]]'
        '//p[contains(@class, "counter_counter__num")]',
    )

    ORDER_CLOSE_BUTTON = (
        By.XPATH,
        '//p[text()="идентификатор заказа"]'
        '/parent::div/parent::div//button',
    )