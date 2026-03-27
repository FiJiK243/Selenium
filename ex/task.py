# Перед запуском убедись что создал виртуальное окружение с помощью команды python3 -m venv .venv
# Активировал виртуальное окружение с помощью . .venv/bin/activate если ты на linux и .venv\Scripts\activate.bat если на windows
# Также установи selenium командой pip install selenium или python3 -m pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    print("Выбери 1 или 2")
    print('1. проверить ссылку "http://suninjuly.github.io/registration1.html"')
    print('2. проверить ссылку "http://suninjuly.github.io/registration2.html"')
    choice = int(input())
    print("выполняется")
    # Если у тебя другой браузер, не Firefox, а Chrome, то просто замени Firefox() на Chrome()
    browser = webdriver.Firefox()
    if choice == 1:
        # Это первая ссылка, она успешно проходит регистрацию
        browser.get("http://suninjuly.github.io/registration1.html")
    elif choice == 2:
        # Это вторая ссылка, она не проходит регистрацию
        browser.get("http://suninjuly.github.io/registration2.html")

    browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input").send_keys(
        "Имя ответ"
    )
    browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input").send_keys(
        "Фамилия ответ"
    )
    browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input").send_keys(
        "Почта ответ"
    )

    # Нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
