from locators.home_page_locators import HomePageLocators
from conftest import driver
from pages.home_page import HomePage
from data import HomePageFAQ
import pytest
import allure


class TestFAQ:
    @allure.title('Проверка соответсвия вопрос-ответ из выпадающего списка «Вопросы о важном»')
    @pytest.mark.parametrize('number, answer', HomePageFAQ.answers)
    def test_faq(self, driver, number, answer):
        home_page = HomePage(driver)
        home_page.open_page()
        home_page.get_cookie(HomePageLocators.COOKIE)
        home_page.find_element(HomePageLocators.LAST_QUESTION)
        home_page.click_question(number)
        assert home_page.get_answer(number) == answer