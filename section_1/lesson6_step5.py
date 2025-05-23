import time
import math

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"
link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
# print(link_text)

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Find the link with calculated text and click it
    link = browser.find_element(By.XPATH, f"//a[contains(text(), {link_text})]")
    link.click()

    # Fill out the form
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    # Click submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit

#
