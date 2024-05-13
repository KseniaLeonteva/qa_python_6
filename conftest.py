import pytest
from selenium import webdriver
from data import Url
from pages.home_page import HomePage
from pages.order_page import OrderPage


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def home_page(driver):
    return HomePage(driver)


@pytest.fixture(scope='function')
def order_page(driver):
    return OrderPage(driver)