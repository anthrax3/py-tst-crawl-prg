from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import configparser
#import pyperclip

from ex_audio import speech_to_text_wit_ai, save_link_to_wav

# получение настроек для прокси
namefile_cfg='config.ini'
config = configparser.ConfigParser()
config.read(namefile_cfg)
server_proxy = config['proxy']['server']
port_proxy = int(config['proxy']['port'])

print(server_proxy)
print(port_proxy)
# END получение настроек для прокси

# настройка данных
# первая страница
ichbin = "ein Mann"
ichsuche = "eine Frau"

geburtsdatum = "1.02.1981"
tag="1"
monat="Februar"
jahr="1981"
# вторая страница
location="Berlin, Germany"
# третья страница
pseudonym = "dows2wsss12"
email = "ii@yandexwq.de"
passw = "Qqwe123!!!!"
kakuznalionas= "Zeitschrift/Zeitung/Magazin"
# END настройка данных

user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101"
# настройка  Chrome
options = webdriver.ChromeOptions()
options.add_argument("test-type")
#options.add_argument('headless')
# set the window size
#options.add_argument('ignore-certificate-errors')
options.add_argument('window-size=1200x600')

# настройка firefox
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", server_proxy)
profile.set_preference("network.proxy.http_port", port_proxy)
profile.update_preferences()
driver = webdriver.Firefox(firefox_profile=profile)
# END настройка firefox
#driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.lovescout24.de/')
driver.implicitly_wait(3)

# первая страница регистрации
elem_username = driver.find_elements_by_css_selector('.regform__kvk-field-group:nth-child(1) .regform__kvk-field-input')
print(elem_username)
elem_username[0].send_keys(ichbin)

elem_username = driver.find_elements_by_css_selector('.regform__kvk-field-group+ .regform__kvk-field-group .regform__kvk-field-input')
print(elem_username)
elem_username[0].send_keys(ichsuche)

elem_username = driver.find_elements_by_css_selector('.regform__dateofbirth-input--day')
print(elem_username)
elem_username[0].send_keys(tag)

elem_username = driver.find_elements_by_css_selector('.regform__dateofbirth-input--month')
print(elem_username)
elem_username[0].send_keys(monat)

elem_username = driver.find_elements_by_css_selector('.regform__dateofbirth-input--year')
print(elem_username)
elem_username[0].send_keys(jahr)

time.sleep(1)

elem_username = driver.find_elements_by_css_selector('button[class*="regform-next-button"]')
print(elem_username)
elem_username[0].click()

#вторая страница регистрации
time.sleep(2)
elem_username = driver.find_elements_by_css_selector('.regform__location-field__input--normal')
print(elem_username)
elem_username[0].send_keys(location)
time.sleep(2)
elem_username[0].send_keys(Keys.DOWN)
elem_username[0].send_keys(Keys.RETURN)
time.sleep(2)
elem_username = driver.find_elements_by_css_selector('button[class*="regform-next-button"]')
print(elem_username)
elem_username[0].click()
time.sleep(2)

#третья страница регистрации

#regform__nickname-field
elem_username = driver.find_elements_by_css_selector('input[name="nickname"]')
print(elem_username)
elem_username[0].send_keys(pseudonym)


#regform__field-label--normal
elem_username = driver.find_elements_by_css_selector('input[name="log"]')
print(elem_username)
elem_username[0].send_keys(email)
time.sleep(1)

elem_username = driver.find_elements_by_css_selector('input[class*="regform__password-field__input--normal"]')
print(elem_username)
elem_username[0].send_keys(passw)
time.sleep(1)

# о том как узнали о сервисе
elem_username = driver.find_elements_by_css_selector('select[class*="regform__survey-field-input"]')
print(elem_username)
try:
    elem_username[0].click()
    time.sleep(1)
    elem_username[0].send_keys(Keys.DOWN)
    elem_username[0].send_keys(Keys.RETURN)
except IndexError:
    pass

time.sleep(3)

elem_username = driver.find_elements_by_css_selector('button[class="button--normal regform-next-button"]')
print(elem_username)
elem_username[0].click()

time.sleep(3)


# решение решение капчи (аудио)
audio_button_coord = pyautogui.locateCenterOnScreen("png/audio_button.png")
pyautogui.moveTo(audio_button_coord)
pyautogui.click()
time.sleep(2)
main_window = driver.current_window_handle

# открываем ссылку на звуковой файл во вкладке
download_audio_button_coord = pyautogui.locateCenterOnScreen("png/audio_download.png")
pyautogui.moveTo(download_audio_button_coord)
pyautogui.click()
time.sleep(2)

# получение ссылки на звуковой файл
driver.switch_to_window(driver.window_handles[1])
link_audio_file = driver.current_url
print("ССылка из окна: ", link_audio_file)
pyautogui.hotkey("ctrl","w")
driver.switch_to_window(main_window)
print("Текущая ссылка: ", driver.current_url)

# сохранения звукового файла и распознование аудио капчи
save_link_to_wav(link_audio_file, "audio_cap.wav")
audio_output = speech_to_text_wit_ai("audio_cap.wav")
#audio_output = speech_to_text_google("audio_cap.wav")
print("Аудио Капча: ", audio_output)
# END решение решение капчи (аудио)

# ввод в строку для ввода ответа
stroka_audio_coord = pyautogui.locateCenterOnScreen("png/stroka_vvoda_otveta.png")
pyautogui.moveTo(stroka_audio_coord)
pyautogui.click()
for l in audio_output:
    pyautogui.press(l)
time.sleep(1)

# клик по кнопке Verify
verify_button_coord = pyautogui.locateCenterOnScreen("png/verify_buttoin.png")
pyautogui.moveTo(verify_button_coord)
pyautogui.click()

#driver.close()