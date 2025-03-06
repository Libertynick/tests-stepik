from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.XPATH, "//img[@src='images/chest.png']")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    y_element = browser.find_element(By.XPATH, "//input[@id='answer']")
    y_element.send_keys(y)
    click_robo = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    click_robo.click()
    click_rob_rule = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    click_rob_rule.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)