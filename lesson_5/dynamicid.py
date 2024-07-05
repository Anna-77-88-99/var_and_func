from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("http://uitestingplayground.com/dynamicid")

button_element = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")
button_element.click()

for i in range(3):
    button_element.click()

sleep(10)