from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), '$100'))
button = browser.find_element(By.XPATH, "//button[@id='book']")
button.click()
x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
x = x_element.text
y = calc(x)
y_element = browser.find_element(By.XPATH, "//input[@id='answer']")
y_element.send_keys(y)

# Отправляем заполненную форму
button = browser.find_element(By.XPATH, "//button[@type='submit']")
button.click()

time.sleep(30)