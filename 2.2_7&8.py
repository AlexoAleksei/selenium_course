import time
import math
import os 
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Remilia")
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Scarlet")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("RemScarlet@ayamail.gensokyo")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, "data.txt")           # добавляем к этому пути имя файла 
    path = browser.find_element(By.ID, "file")
    path.send_keys(file_path)
    
    button = browser.find_element(By.CLASS_NAME, "btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()