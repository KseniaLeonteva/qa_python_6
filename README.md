# UI tests for Яндекс Самокат

## Фикстуры - ***conftest.py***
* `driver` - настройки webdriver

## Набор тестовых данных, список URL - ***data.py***
* `class Users` - валидные данные пользователя
* `class Url` - список URL страниц
* `class HomePageFAQ` - массив ответов на вопросы

## Сценарии, покрытые тестами

### Соответсвие ответов вопросам в разделе "Вопросы о важном" - ***test_FAQ.py***
* `test_FAQ` - проверка соответсвия вопрос-ответ из выпадающего списка «Вопросы о важном»


### Редирект - ***test_home_page.py***
* `test_redirect_scooter_logo` - перенаправление на главную страницу "Яндекс Самокат" при клике на лого "Самокат"
* `test_redirect_yandex_logo` - перенаправление на главную страницу "Дзен" при клике на лого "Яндекс"


### Создание заказа с разными точками входа - ***test_order_page.py***
* `test_create_order_header_button` - создать заказ через кнопку "Заказать" в хедере
* `test_create_order_page_button` - создать заказ через кнопку "Заказать" на странице


## Для запуска:
* Установить зависимости
``` shell
pip3 install -r requirements.txt
```
* Запустить все тесты из директории tests
```shell
pytest tests --alluredir=allure_results
```
* Посмотреть отчет
``` shell
allure serve allure_results
```
