# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ
# 28.971872586834195

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)

    # нажимаем на кнопку
    button = browser.find_element(By.XPATH, "//button")
    button.click()
    time.sleep(1)

    # переход на вторую вкладку
    # метод window_handles, который возвращает массив имён всех вкладок.
    # Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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