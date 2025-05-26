from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time
import math


def safe_eval(expr, x):
    # Define allowed names
    allowed_names = {
        "abs": abs,
        "math": math,
        "sin": math.sin,
        "log": math.log,
        "ln": math.log,  # allow ln as alias to math.log
    }

    # Replace ln with log (Python syntax)
    expr = expr.replace("ln", "log")

    # Replace 'x' with its actual value
    expr = expr.replace("x", str(x))

    # Evaluate
    return str(eval(expr, {"__builtins__": None}, allowed_names))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)


try:
    # Find the button and click on it
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface.btn.btn-primary")
    button.click()

    # Switch to the newly opened window
    browser.switch_to.window(browser.window_handles[1])

    # Locate the value of x by using element's unique ID
    x = int(browser.find_element(By.ID, "input_value").text)

    # Get string of the formula
    label_text = browser.find_element(
        By.XPATH,
        "//*[@id='input_value']/preceding-sibling::span[contains(text(), 'What is')]",
    ).text.lower()
    # Carve formula out of the string
    formula = label_text.split("what is ")[1].split(", where x")[0].strip()
    # Evaluate the answer
    answer = safe_eval(formula, x)

    # Find text input are for the answer and send answer to it
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(answer)

    # Find and click the submit button
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()
finally:
    time.sleep(5)
    browser.quit()
