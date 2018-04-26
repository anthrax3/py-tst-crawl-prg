"""
    использование сервиса для распознования звукового файла в текст
"""

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
import pyautogui


user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101"

# настройка  Chrome
options = webdriver.ChromeOptions()
options.add_argument("test-type")
#options.add_argument('headless')
# set the window size
#options.add_argument('ignore-certificate-errors')
options.add_argument('window-size=1200x600')

#driver = webdriver.Firefox()
driver = webdriver.Chrome(chrome_options=options)
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
path_dir = ""
path_filename = "test.mp3"
elem = driver.find_elements_by_css_selector('div[id="uploader"] input[type="file"]')
print(elem)
elem[0].send_keys("test.mp3")
time.sleep(2)
elem = driver.find_elements_by_css_selector('button[class*="ml-2 mb-3 text--lower btn btn--raised primary"]')
#print(elem)
elem[0].click()
time.sleep(1)

elem = driver.find_elements_by_css_selector('div[class="list__tile__title pt-1"]')
for el in elem:
    print(el.text)

#
