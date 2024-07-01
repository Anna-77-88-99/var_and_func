from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")

input_login = driver.find_element(By.XPATH, "//input[@type='text']")
input_login.send_keys("tomsmith")

input_password = driver.find_element(By.XPATH, "//input[@type='password']")
input_password.send_keys("SuperSecretPassword!")

submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_btn.click()

sleep(10)