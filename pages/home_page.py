from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from data import Url


class HomePage(BasePage):
    def click_question(self, number):
        method, locator = HomePageLocators.QUESTION
        locator = locator.format(number)
        return self.click_on_element((method, locator))


    def get_answer(self, number):
        method, locator = HomePageLocators.ANSWER
        locator = locator.format(number)
        return self.get_text((method, locator))


    def open_page(self):
        self.driver.get(Url.SCOOTER_HOME_PAGE)

