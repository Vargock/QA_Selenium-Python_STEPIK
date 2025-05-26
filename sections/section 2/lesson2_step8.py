from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time
import os

fake = Faker()

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "file.txt")

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

try:
    first_name = browser.find_element(By.NAME, "firstname")
    last_name = browser.find_element(By.NAME, "lastname")
    email = browser.find_element(By.NAME, "email")
    file_send = browser.find_element(By.NAME, "file")
    button = browser.find_element(By.CLASS_NAME, "btn-primary")

    first_name.send_keys(fake.first_name())
    last_name.send_keys(fake.last_name())
    email.send_keys(fake.email())
    file_send.send_keys(file_path)
    time.sleep(1)

    button.click()
finally:
    time.sleep(5)
    browser.quit()
