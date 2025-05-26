from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from faker import Faker
import time
import math


# Dictionary for tying selectors' symbols to anonymous lambda functions
ops = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "×": lambda x, y: x * y,
    "÷": lambda x, y: x / y,
}


# Evaluates answer for this page
def eval(x, y, operator):
    try:
        return ops[operator](x, y)
    except Exception as e:
        print(e)
        return None


browser = webdriver.Chrome()
link = "https://suninjuly.github.io/selects1.html"
browser.get(link)


def run_test():
    try:
        # Grab values of two numbers using their unique IDs
        x = int(browser.find_element(By.ID, "num1").text)
        y = int(browser.find_element(By.ID, "num2").text)

        # Grab operator between the numbers using his position right after NUM1
        operator = browser.find_element(
            By.CSS_SELECTOR, "span#num1 + span.nowrap"
        ).text.strip()

        # Evaluate answer
        answer = eval(x, y, operator)

        # Locate selector
        selector = Select(
            browser.find_element(
                By.XPATH,
                "//label[contains(text(), 'Choose the correct answer:')]/following-sibling::select",
            )
        )

        # Select correct answer by comparing answer to visible text of options
        selector.select_by_visible_text(str(answer))

        # Enable and click the submit button
        submit_btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_btn.click()
    finally:
        time.sleep(5)
        browser.quit()


if __name__ == "__main__":
    run_test()
