from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, browser):
        self.driver = browser

    def get(self):
        self.driver.get("https://www.labirint.ru/cart/")

    def get_counter(self):
        txt = self.driver.find_element(By.CSS_SELECTOR, "a[data-event-label='myCart']").find_element(By.CSS_SELECTOR, 'b').text
        return int(txt)