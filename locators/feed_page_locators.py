from selenium.webdriver.common.by import By


class FeedPageLocators:
    FIRST_ORDER = (
        By.XPATH,
        '(//a[starts-with(@href, "/feed/")])[1]',
    )
    OPENED_ORDER_NUMBER = (
        By.CSS_SELECTOR,
        'section.Modal_modal_opened__3ISw4 '
        'div.Modal_orderBox__1xWdi > p:first-child',
    )
    OVERLAY = (
        By.CSS_SELECTOR,
        'div.Modal_modal_overlay__x2ZCr',
    )

    ORDER_NUMBER = (
        '//a[starts-with(@href, "/feed/")]'
        '//p[starts-with(normalize-space(), "#")]'
        '[number(substring-after(normalize-space(), "#")) = {number}]'
    )

    TOTAL_COMPLETED = (
        By.XPATH,
        '//p[text()="Выполнено за все время:"]/following-sibling::p',
    )
    TODAY_COMPLETED = (
        By.XPATH,
        '//p[text()="Выполнено за сегодня:"]/following-sibling::p',
    )

    IN_PROGRESS_LIST = (
        By.CSS_SELECTOR,
        'ul.OrderFeed_orderListReady__1YFem',
    )

    ORDER_BY_HREF = '//a[@href="{href}"]'