from conftest import driver
from pages.home_page import HomePage
from locators.home_page_locators import HomePageLocators
from data import Url
import allure


class TestHeaderLogo:
    @allure.title('Клик на лого Самоката в шапке открывает главную страницу')
    def test_redirect_scooter_logo(self, driver):
        home_page = HomePage(driver)
        home_page.open_page()
        home_page.click_on_element(HomePageLocators.HEADER_ORDER_BUTTON)
        home_page.click_on_scooter_logo()
        home_page.cross_url(Url.SCOOTER_HOME_PAGE)
        assert driver.current_url == Url.SCOOTER_HOME_PAGE


    @allure.title('Клик на лого Яндекс в шапке открывает главную страницу Dzen')
    def test_redirect_yandex_logo(self, driver):
        home_page = HomePage(driver)
        home_page.open_page()
        home_page.click_on_yandex_logo()
        home_page.tab_switch(driver)
        home_page.cross_url(Url.DZEN_HOME_PAGE)
        assert driver.current_url == Url.DZEN_HOME_PAGE

