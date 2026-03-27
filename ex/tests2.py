from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Firefox()
    browser.get(link)

    # вычисляем текст ссылки
    link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))

    # находим ссылку и кликаем
    browser.find_element(By.LINK_TEXT, link_text).click()

    # заполняем форму
    browser.find_element(By.NAME, "first_name").send_keys("Артем")
    browser.find_element(By.NAME, "last_name").send_keys("Страшко")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Moscow")
    browser.find_element(By.ID, "country").send_keys("Russia")

    # отправляем форму
    time.sleep(0.5)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

finally:
    time.sleep(100)
    browser.quit()
