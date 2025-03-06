from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "[id = 'num1']")
    x = int(x_element.text)
    y_element = browser.find_element(By.CSS_SELECTOR, "[id = 'num2']")
    y = int(y_element.text)
    a = str(x + y)
    select = Select(browser.find_element(By.CSS_SELECTOR, "[class='custom-select']"))
    select.select_by_value(a)

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)