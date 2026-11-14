from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).text

    def fill(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def wait_for_url(self, url):
        return WebDriverWait(self.driver, 10).until(
            EC.url_to_be(url)
        )

    def wait_until_hidden(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(locator)
        )

    def click_when_uncovered(self, locator, overlay_locator):
        def try_click(driver):
            try:
                overlays = driver.find_elements(*overlay_locator)
                if any(overlay.is_displayed() for overlay in overlays):
                    return False

                element = EC.element_to_be_clickable(locator)(driver)
                if not element:
                    return False

                element.click()
                return True
            except (
                ElementClickInterceptedException,
                StaleElementReferenceException,
            ):
                return False

        WebDriverWait(self.driver, 10).until(try_click)

    def click_when_ready(self, locator):
        def try_click(driver):
            try:
                element = EC.element_to_be_clickable(locator)(driver)
                if not element:
                    return False

                element.click()
                return True
            except (
                ElementClickInterceptedException,
                StaleElementReferenceException,
            ):
                return False

        WebDriverWait(self.driver, 10).until(try_click)

    def get_current_tab(self):
        return self.driver.current_window_handle

    def open_new_tab(self, url):
        self.driver.switch_to.new_window('tab')
        self.driver.get(url)
        return self.driver.current_window_handle

    def switch_to_tab(self, handle):
        self.driver.switch_to.window(handle)