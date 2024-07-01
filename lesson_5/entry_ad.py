from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/entry_ad")

button_element = WebDriverWait(driver, 10).until(ExpC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal-footer")))
button_element.click()

sleep(10)