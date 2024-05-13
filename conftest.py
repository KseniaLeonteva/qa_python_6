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

