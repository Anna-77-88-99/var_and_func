import allure
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, browser):
        self.driver = browser
    with allure.step("Переходим в корзину"):
        def get(self):
            self.driver.get("https://www.labirint.ru/cart/")
    with allure.step("Получаем значение из корзины"):
        def get_counter(self) -> int:
            txt = self.driver.find_element(By.CSS_SELECTOR, "a[data-event-label='myCart']").find_element(By.CSS_SELECTOR, 'b').text
            return int(txt)