from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element(By.XPATH, "//input[@id='answer']")
    y_element.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)