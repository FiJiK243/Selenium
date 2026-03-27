from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Firefox()
browser.get("http://suninjuly.github.io/alert_accept.html")

# 1. Нажимаем на кнопку
button = browser.find_element(By.TAG_NAME, "button")
button.click()

# 2. Принимаем confirm
alert = browser.switch_to.alert
alert.accept()

# 3. Ждём, пока появится число x
x_element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "input_value"))
)
x = float(x_element.text)

# 4. Вычисляем ответ
answer = math.log(abs(12 * math.sin(x)))

# 5. Ждём, пока поле для ответа будет доступно, и вводим ответ
answer_input = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "answer"))
)
answer_input.send_keys(str(answer))

# 6. Отправляем форму
submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
submit_button.click()

# 7. Ждём alert с результатом и выводим текст
result_alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
print(result_alert.text)  # Здесь твой ответ с капчи
result_alert.accept()  # Закрываем alert

# Закрываем браузер
browser.quit()
