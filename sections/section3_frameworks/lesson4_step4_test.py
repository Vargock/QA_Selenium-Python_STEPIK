import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker

fake = Faker()

INPUTS = {
    "first name": (
        "//label[text()='First name*']/following-sibling::input",
        fake.first_name(),
    ),
    "last name": (
        "//label[text()='Last name*']/following-sibling::input",
        fake.last_name(),
    ),
    "email": ("//label[text()='Email*']/following-sibling::input", fake.email()),
}

SUCCESS_TEXT = "Congratulations! You have successfully registered!"
URLS = (
    "https://suninjuly.github.io/registration1.html",
    "https://suninjuly.github.io/registration2.html",
)


@pytest.fixture
def browser():
    print("\nStarting browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    yield browser
    print("\nQuitting browser...")
    browser.quit()


@pytest.mark.parametrize("url", URLS)
def test_registration(url, browser):
    browser.get(url)

    elements = []

    for label, (xpath, keys) in INPUTS.items():
        element = browser.find_element(By.XPATH, xpath)
        element.clear()
        element.send_keys(keys)
        elements.append((element, keys, label))

    browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]").click()
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    assert welcome_text == SUCCESS_TEXT
