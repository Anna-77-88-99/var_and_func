import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage

@allure.id("LABIRINT-1")
@allure.epic("Книжный магазин")
@allure.severity("blocker")
@allure.suite("Тест для проверки работы поиска")
@allure.story("Выполнить поиск по слову Python")
@allure.title("Поиск по слову Python")
@allure.feature("READ")
def test_cart_counter():
    with allure.step("Открытие веб-страницы Chrome"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Создание переменной, которая хранит экзампляр класса MainPage"):
        main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.serch("Python")
    with allure.step("Создание переменной, которая хранит экзампляр класса ResultPage"):
        result_page = ResultPage(browser)
    to_be = result_page.add_books()
    with allure.step("Создание переменной, которая хранит экзампляр класса CartPage"):
        cart_page = CartPage(browser)
    cart_page.get() 
    as_is = cart_page.get_counter()
    with allure.step("Сравниваем значения из результата поиска и корзины"):
        assert as_is == to_be
    browser.quit()

@allure.id("LABIRINT-2")
@allure.epic("Книжный магазин")
@allure.severity("blocker")
@allure.suite("Тест для проверки работы поиска")
@allure.story("Выполнить поиск с пустым значением")
@allure.title("Поиск с пустым значением")
@allure.feature("READ")
def test_empty_search():
    with allure.step("Открытие веб-страницы Chrome"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Создание переменной, которая хранит экзампляр класса MainPage"):
        main_page = MainPage(browser) 
    main_page.set_cookie_policy()
    main_page.serch("no book search term")
    with allure.step("Создание переменной, которая хранит экзампляр класса ResultPage"):
        result_page = ResultPage(browser)
    msg = result_page.get_empty_result_message()
    with allure.step("Проверяем значение в случае поиска с пустым значением"):
        assert msg == "Мы ничего не нашли по вашему запросу! Что делать?"
    browser.quit()