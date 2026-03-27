from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


# Функция для решения математической задачи
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# Настройка драйвера
browser = webdriver.Firefox()  # или Firefox, если используете geckodriver
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    # Ждем, когда цена станет $100 (ожидание минимум 12 секунд)
    price_element = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Находим значение x для математической задачи
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Решаем задачу
    answer = calc(x)

    # Вводим ответ
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(answer)

    # Отправляем форму
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    # Даем время увидеть результат, потом закрываем браузер
    import time

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
    time.sleep(5)
    browser.quit()
