# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book", после этого внизу появится задача
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)

    # ждем цену = 100, ожидание 12 сек
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )

    # нажимаем на кнопку
    button = browser.find_element(By.XPATH, "//button[text()='Book']")
    button.click()
    time.sleep(1)

    # поиск значения х на странице и подставление его в функцию calc
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    # поиск поля ввода и вводи полученного значения
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    time.sleep(1)

    # Отправляем
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # копирование текста из всплывающего окна с ответом и вывод ответа
    alert_text = browser.switch_to.alert.text
    print(alert_text.split(': ')[-1])
    browser.switch_to.alert.accept()
    # закрываем браузер после всех манипуляций
    browser.quit()

# ffffffff