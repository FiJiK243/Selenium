from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# Функция для расчета значения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Запуск браузера
browser = webdriver.Firefox()

try:
    # Открываем страницу
    browser.get("https://suninjuly.github.io/math.html")

    # Находим значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Вводим ответ
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # Выбираем radiobutton "Robots rule!"
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_radio.click()

    # Нажимаем Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

    # Ждем появления alert и считываем текст
    time.sleep(1)
    alert = browser.switch_to.alert
    print(alert.text)  # сюда будет выводиться число, которое нужно скопировать

finally:
    time.sleep(3)
    browser.quit()
