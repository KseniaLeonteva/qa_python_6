from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = [By.XPATH, './/input[@placeholder = "* Имя"]'] #поле ввода *Имя
    LAST_NAME_FIELD = [By.XPATH, './/input[@placeholder = "* Фамилия"]'] #поле ввода *Фамилия
    ADDRESS_FIELD = [By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]'] #поле ввода *Адрес: куда привезти заказ
    METRO_FIELD = [By.XPATH, './/input[@placeholder = "* Станция метро"]'] #поле ввода *Станция метро
    STATION_METRO_1 = [By.XPATH, '//li[@class="select-search__row" and @data-index="0" and @data-value="1"]']
    STATION_METRO_2 = [By.XPATH, '//li[@class="select-search__row" and @data-index="5" and @data-value="6"]']
    PHONE_FIELD = [By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]'] #поле ввода *Телефон: на него позвонит курьер
    FURTHER_BUTTON = [By.XPATH, './/button[text() = "Далее"]'] #кнопка "Далее"
    DATE_FIELD = [By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]'] #поле ввода *Когда привезти самокат
    DATE_1 = [By.XPATH, './/div[@class = "react-datepicker__day react-datepicker__day--024"]']
    DATE_2 = [By.XPATH, './/div[@class = "react-datepicker__day react-datepicker__day--023"]']
    PERIOD_FIELD = [By.XPATH, './/div[@class = "Dropdown-placeholder"]'] #поле ввода *Срок аренды
    PERIOD_1 = [By.XPATH, './/div[@class="Dropdown-option" and text()="сутки"]']
    PERIOD_2 = [By.XPATH, './/div[@class="Dropdown-option" and text()="четверо суток"]']
    COLOR_BLACK = [By.XPATH, './/label[@for = "black"]']
    COLOR_GREY = [By.XPATH, './/label[@for = "grey"]']
    COMMENT_FIELD = [By.XPATH, './/input[@placeholder = "Комментарий для курьера"]'] #поле ввода Комментарий для курьера
    ORDER_BUTTON = [By.XPATH, '//*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]'] #кнопка "Заказать"
    YES_BUTTON = [By.XPATH, './/button[text() = "Да"]'] #кнопка "Да"
    MODAL_SCREEN_SUCCESS = [By.XPATH, './/div[@class = "Order_Modal__YZ-d3"]'] #всплывающее окно Заказ оформлен
    LOGO_SCOOTER = [By.XPATH, './/a[@href = "/"]'] #лого Самокат
    LOGO_YANDEX = [By.XPATH, './/a[@href = "//yandex.ru"]'] #лого Яндекс

