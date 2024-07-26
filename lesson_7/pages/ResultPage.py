from selenium.webdriver.common.by import By

class ResultPage:
    def __init__(self, browser):
        self.driver = browser

    def add_books(self):
        self.driver.implicitly_wait(10)
        buy_buttons = self.driver.find_elements(By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")

        counter = 0
        for btn in buy_buttons:
            btn.click()
            counter += 1

        return counter
    
    def get_empty_result_message(self):
        txt = self.driver.find_element(
        By.CSS_SELECTOR, "div.search-error").find_element(By.CSS_SELECTOR, 'h1').text
        return txt