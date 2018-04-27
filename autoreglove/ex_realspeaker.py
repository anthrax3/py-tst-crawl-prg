"""
    использование сервиса для распознования звукового файла в текст
"""

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
import pyautogui
import os


user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101"

# настройка  Chrome
options = webdriver.ChromeOptions()
options.add_argument("test-type")
#options.add_argument('headless')
# set the window size
#options.add_argument('ignore-certificate-errors')
options.add_argument('window-size=1200x600')

driver = webdriver.Firefox()
#driver = webdriver.Chrome(chrome_options=options)
#driver = webdriver.Chrome()
driver.get('https://www.realspeaker.net/')
time.sleep(2)
#driver.implicitly_wait(3)

# первая страница регистрации
elem = driver.find_elements_by_css_selector('button[class*="ml-2 mb-3 btn btn--raised success"]')
#print(elem)
elem[0].click()
time.sleep(1)
# указываем путь до файла
path_dir = os.getcwd()+"/mp3/"
path_filename = "test.mp3"
path_full = path_dir+path_filename
elem = driver.find_elements_by_css_selector('div input[title="file input"]')
print(elem)
elem[0].send_keys(path_full)
time.sleep(2)
elem = driver.find_elements_by_css_selector('button[class*="ml-2 mb-3 text--lower btn btn--raised primary"]')
#print(elem)
elem[0].click()
time.sleep(1)

elem = driver.find_elements_by_css_selector('div[class="list__tile__title pt-1"]')
elem_button = driver.find_elements_by_css_selector('div[class="list__tile__action text-xs-right"] button[class="btn btn--raised btn--small primary"]')
print(len(elem))
print(len(elem_button))
for i in range(0, len(elem)):
    if elem[i].text.strip()==path_filename:
        elem_button[i].click()
        break
time.sleep(5)

elem = driver.find_elements_by_css_selector('div[class="list__tile__title pt-1"]')
elem_button = driver.find_elements_by_css_selector('div[class="list__tile__action text-xs-right"] button[class="btn btn--raised success"]')
print(len(elem))
print(len(elem_button))
for i in range(0, len(elem)):
    if elem[i].text.strip()==path_filename:
        elem_button[i].click()
        break


# преход ко второй странице (списка файлов на транскрипцию)

