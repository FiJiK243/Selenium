from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

browser: None|webdriver.Firefox = None
try:
    browser = webdriver.Firefox()
    browser.get(link)
    value1 = ""
    value2 = ""
    value3 = ""

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Артем")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Страшко")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Moscow")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    if isinstance(browser, webdriver.Firefox):
        time.sleep(30)
        browser.quit()
    # успеваем скопировать код за 30 секунд

# не забываем оставить пустую строку в конце файла
