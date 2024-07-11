from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support. ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

#insialisasi
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
admin = "oxd-main-menu-item"
driver.get("https://google.com")

#perintah untuk pencarian website orangehrm pada search bar google
WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("orangehrmlive" + Keys.ENTER)

#perintah untuk masuk kedalam website orangehrm
WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "OrangeHRM"))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "OrangeHRM")
link.click()

#perintah untuk mengisi username pada kolom login pada website orangehrm
WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.NAME, "username"))
)
input_element = driver.find_element(By.NAME, "username")
input_element.clear()
input_element.send_keys("Admin")

#perintah untuk mengisi password pada kolom login pada website orangehrm
WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.NAME, "password"))
)
input_element = driver.find_element(By.NAME, "password")
input_element.clear()
input_element.send_keys("admin123" + Keys.ENTER)

#perintah untuk memilih modul admin pada sidebar website orangehrm
WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.CLASS_NAME, admin))
)
adminn = driver.find_element(By.CLASS_NAME, admin)
adminn.click()



time.sleep(10)
driver.quit()