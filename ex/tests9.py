# не работает
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# Запуск браузера
browser = webdriver.Firefox()

try:
    # 1. Открываем страницу
    browser.get("https://SunInJuly.github.io/execute_script.html")

    # 2. Считываем x
    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)

    # 3. Считаем функцию ln(abs(12*sin(x)))
    y = math.log(abs(12 * math.sin(x)))

    # 4. Скроллим страницу вниз, чтобы кнопка Submit стала доступна
    # Используем JS: скролл к элементу
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("arguments[0].scrollIntoView(true);", submit_button)

    # 5. Вводим ответ
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(str(y))

    # 6. Выбираем checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    if not checkbox.is_selected():
        checkbox.click()

    # 7. Переключаем radiobutton "Robots rule"
    robots_radio = browser.find_element(By.ID, "robotsRule")
    if not robots_radio.is_selected():
        robots_radio.click()

    # 8. Нажимаем Submit
    submit_button.click()

    # Ждём, чтобы увидеть результат
    time.sleep(5)

finally:
    time.sleep(100)
