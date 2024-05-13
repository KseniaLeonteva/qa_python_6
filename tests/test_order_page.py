from conftest import driver
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
from data import UserMainOrderButton, UserHeaderButton
import allure




class TestOrderPage:
    @allure.title('Проверка оформления заказа через кнопку "Заказать" в хедере')
    def test_create_order_header_button(self, driver):
        home_page = HomePage(driver)
        home_page.open_page()
        order_page = OrderPage(driver)
        home_page.get_cookie(HomePageLocators.COOKIE)
        order_page.click_header_order_button()
        order_page.create_order(UserHeaderButton.name,
                                UserHeaderButton.last_name,
                                UserHeaderButton.address,
                                OrderPageLocators.STATION_METRO_1,
                                UserHeaderButton.phone,
                                OrderPageLocators.DATE_1,
                                OrderPageLocators.PERIOD_1,
                                OrderPageLocators.COLOR_BLACK,
                                UserHeaderButton.comment)
        assert 'Заказ оформлен' in order_page.check_success_order()

    @allure.title('Проверка оформления заказа через кнопку "Заказать" на странице')
    def test_create_order_page_button(self, driver):
        home_page = HomePage(driver)
        home_page.open_page()
        order_page = OrderPage(driver)
        home_page.get_cookie(HomePageLocators.COOKIE)
        order_page.click_page_button()
        order_page.create_order(UserMainOrderButton.name,
                                UserMainOrderButton.last_name,
                                UserMainOrderButton.address,
                                OrderPageLocators.STATION_METRO_2,
                                UserMainOrderButton.phone,
                                OrderPageLocators.DATE_2,
                                OrderPageLocators.PERIOD_2,
                                OrderPageLocators.COLOR_GREY,
                                UserMainOrderButton.comment)
        assert 'Заказ оформлен' in order_page.check_success_order()