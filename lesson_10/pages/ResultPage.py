import allure
from selenium.webdriver.common.by import By

class ResultPage:
    def __init__(self, browser):
        self.driver = browser
    with allure.step("Добавляем книги в корзину"):
        def add_books(self) -> int:
            self.driver.implicitly_wait(10)
            buy_buttons = self.driver.find_elements(By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")
            counter = 0
            for btn in buy_buttons:
                btn.click()
                counter += 1
            return counter
    with allure.step("Получить сообщение при пустом результате"):    
        def get_empty_result_message(self) -> str:
            txt = self.driver.find_element(
            By.CSS_SELECTOR, "div.search-error").find_element(By.CSS_SELECTOR, 'h1').text
            return txt