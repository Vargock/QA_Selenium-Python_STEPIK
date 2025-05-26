from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/explicit_wait2.html"
browser.get(link)


def safe_eval(expr, x):
    # Define allowed names
    allowed_names = {
        "abs": abs,
        "math": math,
        "sin": math.sin,
        "log": math.log,
        "ln": math.log,  # allow 'ln' as alias to math.log
    }

    expr = expr.replace("ln", "log")  # Replace ln with log (Python syntax)
    expr = expr.replace("x", str(x))  # Replace 'x' with its actual value

    return str(eval(expr, allowed_names))  # Evaluate


try:
    # Find the price, wait until it is $100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    # Find the button and click on it
    button = browser.find_element(By.ID, "book")
    button.click()

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
    submit_btn = browser.find_element(By.ID, "solve")
    submit_btn.click()

finally:
    time.sleep(5)
    browser.quit()
