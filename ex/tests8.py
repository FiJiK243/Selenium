from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Firefox()

try:
    browser.get("https://suninjuly.github.io/selects1.html")

    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)

    result = num1 + num2

    dropdown = Select(browser.find_element(By.ID, "dropdown"))
    dropdown.select_by_value(str(result))

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
