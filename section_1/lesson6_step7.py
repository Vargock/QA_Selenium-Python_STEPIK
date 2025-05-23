from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    fake = Faker()
    count = 0

    elements = browser.find_elements(By.CSS_SELECTOR, "div > input")
    print(f"Found {len(elements)} inputs")
    br_elems = []
    for element in elements:
        el_name = element.get_attribute("name")
        # label_text = preceding_text.text.strip().lower()

        if el_name:
            print(el_name)

        if el_name == "firstname":
            element.send_keys(fake.name())
        elif el_name == "lastname":
            element.send_keys(fake.last_name())
        elif el_name == "e-mail":
            element.send_keys(fake.email())
        else:
            element.send_keys(fake.word())

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
