import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:
    def __init__(self, driver): 
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
    with allure.step("Установка задержки - {time} секунд"):
        def send_time(self, time: int):
            input_delay = self._driver.find_element(By.CSS_SELECTOR, 'input[id = "delay"]')
            input_delay.clear()
            input_delay.send_keys(time)
    with allure.step("Установка ожидания элемента - {driver_time} со значением {expected_value}"):
        def calculate(self, driver_time: str, expected_value: str) -> str:
            self._driver.find_element(By.XPATH, '//span[contains(text(),"7")]').click()
            self._driver.find_element(By.XPATH, '//span[contains(text(),"+")]').click()
            self._driver.find_element(By.XPATH, '//span[contains(text(),"8")]').click()
            self._driver.find_element(By.XPATH, '//span[contains(text(),"=")]').click()
            WebDriverWait(self._driver, driver_time).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), expected_value))
            resalt_value = self._driver.find_element(By.CSS_SELECTOR, "div.screen").text
            return resalt_value