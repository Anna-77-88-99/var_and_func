from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.DataTypes import DataTypes

def test_element_red():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    data_types_page = DataTypes(browser)
    data_types_page.send_data("Иван", "Иванов", "ул. Советская", "ivanivanov@test.com", "8800553535", "", "Москва", "Россия", "Тестировщик", "SkyPro")
    get_red_color = data_types_page.element_color_red()
    red_color = 'rgba(248, 215, 218, 1)'
    assert get_red_color == red_color
    browser.quit()

def test_element_green():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    data_types_page = DataTypes(browser)
    data_types_page.send_data("Иван", "Иванов", "ул. Советская", "ivanivanov@test.com", "8800553535", "", "Москва", "Россия", "Тестировщик", "SkyPro")
    list_of_green = ['rgba(209, 231, 221, 1)'] * 9
    get_green_color = data_types_page.element_color_green()
    assert get_green_color == list_of_green
    browser.quit()