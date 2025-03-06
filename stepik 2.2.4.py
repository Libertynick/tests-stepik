from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.XPATH, '//input[@name="firstname"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//input[@name="lastname"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//input[@name="email"]')
    input3.send_keys("ivpet@yandex.ru")

    # подгрузка файла 
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'pytest.txt')
    
    element = browser.find_element(By.XPATH, '//input[@id="file"]')
    element.send_keys(file_path)
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)