from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.SaucedemoPage import SaucedemoPage

def test_shop():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    shop = SaucedemoPage(browser)
    shop.authorization("standard_user", "secret_sauce")
    shop.choose_product()
    shop.send_user_data("Анна", "Шашкина", "88005553535")
    price = shop.shop_finish()
    assert price == 'Total: $58.29'