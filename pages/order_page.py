from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage



class OrderPage(HomePage):
    def click_header_order_button(self):
        self.click_on_element(HomePageLocators.HEADER_ORDER_BUTTON)


    def click_page_button(self):
        self.click_on_element(HomePageLocators.PAGE_ORDER_BUTTON)

    def set_name(self, name):
        self.send_keys(OrderPageLocators.NAME_FIELD, name)


    def set_last_name(self, last_name):
        self.send_keys(OrderPageLocators.LAST_NAME_FIELD, last_name)


    def set_address(self, address):
        self.send_keys(OrderPageLocators.ADDRESS_FIELD, address)


    def set_metro(self, station_metro):
        self.click_on_element(OrderPageLocators.METRO_FIELD)
        self.click_on_element(station_metro)


    def set_phone(self, phone):
        self.send_keys(OrderPageLocators.PHONE_FIELD, phone)


    def click_further_button(self):
        self.click_on_element(OrderPageLocators.FURTHER_BUTTON)


    def set_date(self, date):
        self.click_on_element(OrderPageLocators.DATE_FIELD)
        self.click_on_element(date)


    def set_period(self, period):
        self.click_on_element(OrderPageLocators.PERIOD_FIELD)
        self.click_on_element(period)


    def set_color(self, color):
        self.click_on_element(color)


    def set_comment(self, comment):
        self.send_keys(OrderPageLocators.COMMENT_FIELD, comment)


    def check_success_order(self):
        return self.get_text(OrderPageLocators.MODAL_SCREEN_SUCCESS)


    def click_order_button(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)


    def click_yes_button(self):
        self.click_on_element(OrderPageLocators.YES_BUTTON)


    def create_order(self, name, last_name, address, station_metro, phone, date, period, color, comment):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro(station_metro)
        self.set_phone(phone)
        self.click_further_button()
        self.set_date(date)
        self.set_period(period)
        self.set_color(color)
        self.set_comment(comment)
        self.click_order_button()
        self.click_yes_button()