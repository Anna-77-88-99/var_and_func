from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
button_element = driver.find_element(By.XPATH, "//button[text()='Add Element']")
for i in range(5):
    button_element.click()

delete_button = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
print("Размер списка", len(delete_button))

sleep(10)