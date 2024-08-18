import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DataTypes:
    def __init__(self, driver): 
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
    with allure.step("Передача данных в соответсвующие поля {first_name}:{last_name}:{address}:{mail}:{phone}:{zip_code}:{city}:{country}:{job}:{company}"):
        def send_data (self, first_name, last_name, address, mail, phone, zip_code, city, country, job, company):
            self._driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(first_name)
            self._driver.find_element(By.CSS_SELECTOR, 'input[name = "last-name"]').send_keys(last_name)
            self._driver.find_element(By.CSS_SELECTOR, 'input[name = "address"]').send_keys(address)
            self._driver.find_element(By.CSS_SELECTOR, 'input[name = "e-mail"]').send_keys(mail)
            self._driver.find_element(By.CSS_SELECTOR, 'input[name = "phone"]').send_keys(phone)
            self._driver.find_element(By.CSS_SELECTOR, 'input[name = "zip-code"]').send_keys(zip_code)
            self._driver.find_element(By.CSS_SELECTOR, 'input[name = "city"]').send_keys(city)
            self._driver.find_element(By.CSS_SELECTOR, 'input[name = "country"]').send_keys(country)
            self._driver.find_element(By.CSS_SELECTOR, 'input[name = "job-position"]').send_keys(job)
            self._driver.find_element(By.CSS_SELECTOR, 'input[name = "company"]').send_keys(company)
            button = self._driver.find_element(By.CSS_SELECTOR, 'button.btn')
            button.click()
    with allure.step("Получение цвета поля ZipCode"):
        def element_color_red (self) -> str:
            zip_code_color = self._driver.find_element(By.CSS_SELECTOR, "div.alert-danger").value_of_css_property("background-color") 
            return zip_code_color
    with allure.step("Получение цвета полей кроме ZipCode"):
        def element_color_green(self) -> list[str]:
            WebDriverWait(self._driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#company")))
            other_fields = ["#first-name", "#last-name", "#address", "#e-mail", "#phone", "#city", "#country", "#job-position", "#company"]
            color_list = []
            for field in other_fields:
                color_list.append(self._driver.find_element(By.CSS_SELECTOR, field).value_of_css_property("background-color"))
            return color_list