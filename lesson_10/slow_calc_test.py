import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalcPage import CalcPage

@allure.id("Calculator-1")
@allure.epic("калькулятор")
@allure.severity("blocker")
@allure.suite("Тесты на работу с калькулятором")
@allure.story("Выполнение математических операций на калькуляторе")
@allure.title("Сложение чисел на калькуляторе")
@allure.feature("CREATE")
def test_element_calc():
    with allure.step("Открытие веб-страницы Chrome"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Создание переменной, которая хранит экзампляр класса CalcPage"):
        calculator = CalcPage(browser)
    calculator.send_time(45)
    ex_value = calculator.calculate("46","15")
    with allure.step("Сравниваем полученое значение"):
        assert ex_value == "15"
    browser.quit()