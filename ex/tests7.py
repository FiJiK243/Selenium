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
    browser.get("http://suninjuly.github.io/get_attribute.html")

    # Находим сундук и считываем значение x из атрибута valuex
    chest = browser.find_element(By.ID, "treasure")
    x = chest.get_attribute("valuex")
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

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

    # Ждем alert и выводим текст с числом
    time.sleep(1)
    alert = browser.switch_to.alert
    print(alert.text)

finally:
     time.sleep(300)
     # browser.quit()
