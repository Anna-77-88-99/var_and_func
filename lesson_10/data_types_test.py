import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.DataTypes import DataTypes

@allure.id("DataType-1")
@allure.epic("Персональные данные")
@allure.severity("blocker")
@allure.suite("Тесты на работу формы с заполнением персональных данных")
@allure.story("Заполнение персональных данных кроме ZipCode")
@allure.title("Заполнить персональные данные")
@allure.feature("CREATE")
def test_element_red():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    data_types_page = DataTypes(browser)
    data_types_page.send_data("Иван", "Иванов", "ул. Советская", "ivanivanov@test.com", "8800553535", "", "Москва", "Россия", "Тестировщик", "SkyPro")
    get_red_color = data_types_page.element_color_red()
    red_color = 'rgba(248, 215, 218, 1)'
    assert get_red_color == red_color
    browser.quit()
@allure.id("DataType-2")
@allure.epic("Персональные данные")
@allure.severity("blocker")
@allure.suite("Тесты на работу формы с заполнением персональных данных")
@allure.story("Заполнение персональных данных кроме ZipCode")
@allure.title("Заполнить персональные данные")
@allure.feature("CREATE")
def test_element_green():
    with allure.step("Открытие веб-страницы Chrome"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Создание переменной, которая хранит экзампляр класса DataTypes"):
        data_types_page = DataTypes(browser)
    data_types_page.send_data("Иван", "Иванов", "ул. Советская", "ivanivanov@test.com", "8800553535", "", "Москва", "Россия", "Тестировщик", "SkyPro")
    list_of_green = ['rgba(209, 231, 221, 1)'] * 9
    get_green_color = data_types_page.element_color_green()
    with allure.step("Сравнение цвета поля у всех полей кроме ZipCode"):
        assert get_green_color == list_of_green
    browser.quit()