from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
import pyautogui

"""
    примеры настройки прокси для браузеров
"""
"""
# настройка  Chrome 
options = webdriver.ChromeOptions()
#options.add_argument('headless')
# set the window size
options.add_argument('window-size=1200x600')
PROXY = "167.99.235.92:3128" # IP:PORT or HOST:PORT
options.add_argument('--proxy-server=http://%s' % PROXY)
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.google.com/')
"""

profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", "189.7.105.138")
profile.set_preference("network.proxy.http_port", 20183)
"""
profile.setPreference("network.proxy.ssl", "proxy.domain.example.com");
profile.setPreference("network.proxy.ssl_port", 8080);
"""
profile.update_preferences()
driver2 = webdriver.Firefox(firefox_profile=profile)
driver2.get('http://ya.ru')
#driver2.get('http://www.linkedin.com/')