from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SwagLabs:

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    driver.find_element(By.CSS_SELECTOR, 'input[name="firstName"]').send_keys("Анна")
    driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]').send_keys("Шашкина")
    driver.find_element(By.CSS_SELECTOR, 'input[name="postalCode"]').send_keys("88005553535")
    driver.find_element(By.CSS_SELECTOR, 'input[name="continue"]').click()
    price_value = WebDriverWait(driver, "10").until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
    driver.find_element(By.CSS_SELECTOR, "#finish").click()
    driver.quit()
    print(price_value)