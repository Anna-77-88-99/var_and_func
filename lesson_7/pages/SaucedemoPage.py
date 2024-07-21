from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SaucedemoPage:
    def __init__(self, driver): 
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def authorization(self, user_name, user_pass):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(user_name)
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(user_pass)
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    def choose_product(self):
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        self._driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    def send_user_data(self, first_name, last_name, zip_code):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="firstName"]').send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]').send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="postalCode"]').send_keys(zip_code)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="continue"]').click()

    def shop_finish(self):
        price_value = WebDriverWait(self._driver, "10").until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
        self._driver.find_element(By.CSS_SELECTOR, "#finish").click()
        return price_value