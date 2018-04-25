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

driver = webdriver.Firefox()
#driver = webdriver.Chrome(chrome_options=options)
#driver = webdriver.Chrome()
driver.get('https://www.realspeaker.net/')

#driver.implicitly_wait(3)

# первая страница регистрации
elem = driver.find_elements_by_css_selector('.success .btn__content')
print(elem)
elem[0].click()