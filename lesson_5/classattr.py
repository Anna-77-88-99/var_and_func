from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("http://uitestingplayground.com/classattr")

button_element = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
button_element.click()
driver.switch_to.alert.accept()

for i in range(3):
    button_element.click()
    driver.switch_to.alert.accept()
sleep(10)