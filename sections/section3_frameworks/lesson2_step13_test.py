import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time

fake = Faker()

# Уникальные селекторы и значения для обязательных полей
INPUTS = {
    "first name": (
        "//label[text()='First name*']/following-sibling::input",
        fake.first_name(),
    ),
    "last name": (
        "//label[text()='Last name*']/following-sibling::input",
        fake.last_name(),
    ),
    "email": (
        "//label[text()='Email*']/following-sibling::input",
        fake.email(),
    ),
}

SUCCESS_TEXT = "Congratulations! You have successfully registered!"
URL = "https://suninjuly.github.io/registration1.html"
# URL = "https://suninjuly.github.io/registration2.html"


class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)  # waits up to 5 seconds

    def tearDown(self):
        self.browser.quit()

    # Получить все поля из переменной INPUTS, вернуть список
    def get_elements(self):
        elements = []

        for label, (xpath, keys) in INPUTS.items():
            element = self.browser.find_element(By.XPATH, xpath)

            elements.append((element, keys, label))

        return elements

    # Заполнить поля значениями
    def fill_inputs(self, inputs: list[tuple]):
        for element, keys, _ in inputs:
            element.clear()
            element.send_keys(keys)

    # Зарегестрироваться
    def submit_form_and_check(self):
        self.browser.find_element(
            By.XPATH, "//button[contains(text(), 'Submit')]"
        ).click()

        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text

        self.assertEqual(welcome_text, SUCCESS_TEXT)

    # Тест
    def run_test_on_url(self, url):
        self.browser.get(url)
        inputs = self.get_elements()
        self.fill_inputs(inputs)
        self.submit_form_and_check()

    def test_registration_page1(self):
        self.run_test_on_url("https://suninjuly.github.io/registration1.html")

    def test_registration_page2(self):
        self.run_test_on_url("https://suninjuly.github.io/registration2.html")


if __name__ == "__main__":
    unittest.main()
