from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator:

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()

    input_delay = driver.find_element(By.CSS_SELECTOR, 'input[id = "delay"]')
    input_delay.clear()
    input_delay.send_keys(45)

    driver.find_element(By.XPATH, '//span[contains(text(),"7")]').click()
    driver.find_element(By.XPATH, '//span[contains(text(),"+")]').click()
    driver.find_element(By.XPATH, '//span[contains(text(),"8")]').click()
    driver.find_element(By.XPATH, '//span[contains(text(),"=")]').click()

    wait_value = WebDriverWait(driver, "46").until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))
    resalt_value = driver.find_element(By.CSS_SELECTOR, "div.screen").text
    
    driver.quit()