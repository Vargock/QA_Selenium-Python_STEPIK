from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time

fake = Faker()

# Уникальные селекторы и значения для обязательных полей
REQUIRED = {
    "first name": (
        "//div[@class='first_block']/div[contains(@class, 'first_class')]/input",
        fake.first_name(),
    ),
    "last name": (
        "//div[@class='first_block']/div[contains(@class, 'second_class')]/input",
        fake.last_name(),
    ),
    "email": (
        "//div[@class='first_block']/div[contains(@class, 'third_class')]/input",
        fake.email(),
    ),
}

# Уникальные селекторы и значения для опциональных полей
OPTIONAL = {
    "phone": (
        "//div[@class='second_block']/div[contains(@class, 'first_class')]/input",
        fake.phone_number(),
    ),
    "address": (
        "//div[@class='second_block']/div[contains(@class, 'second_class')]/input",
        fake.street_address(),
    ),
}

# Текст, использующийся для проверки успешной регистрации
SUCCESS_TEXT = "Congratulations! You have successfully registered!"


# Получить все обязательные и дополнительные поля, вызвать ошибку, если хотя бы одно обязательное поле не найдено
def get_elements(browser):
    required_inputs = []
    optional_inputs = []

    # Получить все обязательные поля, вызвать ошибку, если хотя бы одно обязательное поле не найдено
    for label, (xpath, keys) in REQUIRED.items():
        try:
            element = browser.find_element(By.XPATH, xpath)
            required_inputs.append((element, keys, label))
        except Exception as e:
            print(f"\n❌ Search for an element {label}: {xpath} FAILED | LINE 50\n")
            raise e

    # Получить все дополнительные поля, вызвать ошибку, если хотя бы одно дополнительное поле не найдено
    for label, (xpath, keys) in OPTIONAL.items():
        try:
            element = browser.find_element(By.XPATH, xpath)
            optional_inputs.append((element, keys, label))
        except Exception as e:
            print(f"\n❌ Search for an element {label}: {xpath} FAILED | LINE 60\n")
            raise e

    # Вывести информацию о найденных полях в читаемом виде
    print("\nRequired fields found:")
    for element, value, label in required_inputs:
        print(f" - {label}: {value} [{element}]")
    print("\nOptional fields found:")
    for element, value, label in optional_inputs:
        print(f" - {label}: {value} [{element}]")

    return required_inputs, optional_inputs


# Заполнить поля значениями
def fill_inputs(inputs: list[tuple]):
    for input_field, keys, label in inputs:
        try:
            input_field.send_keys(keys)
        except Exception as e:
            print(f"\n❌ Attempt to fill input {label} has FAILED | LINE 81\n")
            raise e


# Запуск тестов в различных режимах
def run_tests():
    for mode in ("required", "optional", "all"):
        print(f"\n🧪 Running test with mode: '{mode}'")
        # Открыть браузер
        browser = webdriver.Chrome()
        browser.get("https://suninjuly.github.io/registration1.html")

        # Получить поля
        required, optional = get_elements(browser)

        try:
            # Заполнить только обязательные поля
            if mode == "required":
                fill_inputs(required)
                expected_result = True
            # Заполнить только дополнительные поля
            elif mode == "optional":
                fill_inputs(optional)
                expected_result = False
            # Заполнить все поля
            elif mode == "all":
                fill_inputs(required + optional)
                expected_result = True
            # Неверный режим: выберите 'required', 'optional' или 'all'
            else:
                raise ValueError(
                    "Invalid mode: choose 'required', 'optional', or 'all'."
                )

            # Найти и нажать кнопку "Submit"
            browser.find_element(
                By.XPATH, "//button[contains(text(), 'Submit')]"
            ).click()

            # Подождать, пока загрузится новая страница
            time.sleep(1)

            # Проверить текст приветствия на странице
            welcome_text = browser.find_element(By.TAG_NAME, "h1").text
            if expected_result:
                assert welcome_text == SUCCESS_TEXT
            else:
                assert welcome_text != SUCCESS_TEXT

            print(f"✅ Test passed for mode '{mode}' has SUCCEDED")
        except Exception as e:
            print(f"❌ Test failed for mode '{mode}' has FAILED")
            raise e
        # Закрыть браузер
        finally:
            time.sleep(2)
            browser.quit()


if __name__ == "__main__":
    run_tests()
