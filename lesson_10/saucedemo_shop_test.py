import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.SaucedemoPage import SaucedemoPage

@allure.id("Shop-1")
@allure.epic("Интернет магазин")
@allure.severity("blocker")
@allure.story("Покупка товаров")
@allure.feature("CREATE")
@allure.title("Выбор товара, работа с корзиной и оплата")
@allure.suite("Тесты на работу с интернет-магазином")
def test_shop():
    with allure.step("Открытие веб-страницы Chrome"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Создание переменной, которая хранит экзампляр класса SaucedemoPage"):
        shop = SaucedemoPage(browser)
    shop.authorization("standard_user", "secret_sauce")
    shop.choose_product()
    shop.send_user_data("Анна", "Шашкина", "88005553535")
    price = shop.shop_finish()
    with allure.step("Сравнение суммы покупок"):
        assert price == 'Total: $58.29'