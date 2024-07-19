from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DataTypes:

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()

   
    driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, 'input[name = "last-name"]').send_keys("Иванов")
    driver.find_element(By.CSS_SELECTOR, 'input[name = "address"]').send_keys("ул. Советская")
    driver.find_element(By.CSS_SELECTOR, 'input[name = "e-mail"]').send_keys("ivanivanov@test.com")
    driver.find_element(By.CSS_SELECTOR, 'input[name = "phone"]').send_keys("8800553535")
    driver.find_element(By.CSS_SELECTOR, 'input[name = "zip-code"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[name = "city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, 'input[name = "country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, 'input[name = "job-position"]').send_keys("Тестировщик")
    driver.find_element(By.CSS_SELECTOR, 'input[name = "company"]').send_keys("SkyPro")
    button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    red_div = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#zip-code")))
    zip_code_color = driver.find_element(By.CSS_SELECTOR, "div.alert-danger").value_of_css_property("background-color") 

    green_div = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#company")))
    other_fields = ["#first-name", "#last-name", "#address", "#e-mail", "#phone", "#city", "#country", "#job-position", "#company"]
    color_list = []
    for field in other_fields:
        color_list.append(driver.find_element(By.CSS_SELECTOR, field).value_of_css_property("background-color"))

    driver.quit()