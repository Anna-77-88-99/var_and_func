from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalcPage import CalcPage

def test_element_calc():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calculator = CalcPage(browser)
    calculator.send_time(45)
    ex_value = calculator.calculate("46","15")
    assert ex_value == "15"
    browser.quit()