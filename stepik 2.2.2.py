from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def cacl(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = cacl(x)
    y_element = browser.find_element(By.XPATH, "//input[@id='answer']")
    y_element.send_keys(y)
    button = browser.find_element(By.XPATH, "//button[@type='submit']")

    # скрол страницы до видимости
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    click_robo = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    click_robo.click()
    click_rob_rule = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    click_rob_rule.click()
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)