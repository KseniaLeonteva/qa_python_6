from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def find_element(self, locator):
        self.driver.find_element(*locator)


    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()


    def get_text(self, locator):
        return self.driver.find_element(*locator).text


    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)


    def cross_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))


    def click_on_yandex_logo(self):
        self.click_on_element(OrderPageLocators.LOGO_YANDEX)


    def click_on_scooter_logo(self):
        self.click_on_element(OrderPageLocators.LOGO_SCOOTER)


    def get_cookie(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator)).click()


    def tab_switch(self, driver):
        driver.switch_to.window(driver.window_handles[1])

