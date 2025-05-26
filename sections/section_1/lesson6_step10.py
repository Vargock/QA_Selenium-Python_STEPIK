from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

try:
    fake = Faker()
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    try:
        inputs = browser.find_elements(By.CSS_SELECTOR, "input")
        required = [i for i in inputs if i.get_attribute("required") is not None]
        titles = [
            input.find_element(By.XPATH, "preceding-sibling::label").text.lower()
            for input in required
        ]
        required_titles = [
            input.find_element(By.XPATH, "preceding-sibling::label").text.lower()
            for input in inputs
        ]

        for i in range(len(required)):
            if any(word in required_titles[i] for word in ["email", "e-mail"]):
                required[i].send_keys(fake.email())
                time.sleep(1)
            elif "name" in required_titles[i]:
                required[i].send_keys(fake.name())
                time.sleep(1)
            else:
                print(f"{fake.word()}")
                time.sleep(1)

    except Exception as e:
        raise e

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
