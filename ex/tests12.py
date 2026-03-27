from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Firefox()
browser.get("https://suninjuly.github.io/redirect_accept.html")

# Нажимаем кнопку, которая делает редирект
button = browser.find_element(By.TAG_NAME, "button")
button.click()

# Принимаем confirm
alert = browser.switch_to.alert
alert.accept()

# Ждём, пока страница загрузится и input_value изменится
x_element = WebDriverWait(browser, 10).until(
    lambda d: d.find_element(By.ID, "input_value").text.strip()
    != ""  # текст стал не пустым
)
x = float(x_element.text)

# Вычисляем ответ
answer = math.log(abs(12 * math.sin(x)))

# Ждём, пока поле для ответа будет кликабельным, и вводим ответ
answer_input = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "answer"))
)
answer_input.send_keys(str(answer))

# Отправляем форму
submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
submit_button.click()

# Ждём alert с результатом и выводим
result_alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
print(result_alert.text)
result_alert.accept()

browser.quit()
