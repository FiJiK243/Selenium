from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Путь к файлу для загрузки
current_dir = os.path.abspath(os.path.dirname(__file__))  # текущая папка скрипта
file_path = os.path.join(current_dir, "sample.txt")  # файл sample.txt

# Если файла нет, создаём пустой
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("")

# Запуск браузера
browser = webdriver.Firefox()

try:
    # 1. Открываем страницу
    browser.get("http://suninjuly.github.io/file_input.html")

    # 2. Заполняем текстовые поля
    browser.find_element(By.NAME, "firstname").send_keys("Иван")
    browser.find_element(By.NAME, "lastname").send_keys("Петров")
    browser.find_element(By.NAME, "email").send_keys("ivan.petrov@example.com")

    # 3. Загружаем файл
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    # 4. Нажимаем Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Ждём, чтобы увидеть результат
    time.sleep(100)

finally:
    browser.quit()
