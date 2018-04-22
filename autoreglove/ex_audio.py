"""
    модуль для работы с аудио файлами и распознования аудио файлов
"""
import requests
import io
import time
import uuid
from ya_speechkit import speech_to_text_yandex

# Speech Recognition Imports
from pydub import AudioSegment
import speech_recognition as sr
    
def save_audio_from_url(url,namefile='sound.mp3'):
    """
        сохраняет урл айдиофайл в mp3 
    """
    # Download the challenge audio and store in memory
    request = requests.get(url)
    audio_file = io.BytesIO(request.content)

    with open(namefile,'wb') as out: 
        out.write(audio_file.read())
    return namefile
    
def convert_mp3_to_wav(namefile, namefile_wav="tst.wav"):
    """
        конвертация файла в wav формат
    """
    # Convert the audio to a compatible format in memory
    converted_audio = io.BytesIO()
    audio_file = None
    with open(namefile,'rb') as out: 
        audio_file = io.BytesIO(out.read())
    sound = AudioSegment.from_mp3(audio_file)
    sound.export(converted_audio, format="wav")
    converted_audio.seek(0)
    
    with open(namefile_wav,'wb') as out: 
        out.write(converted_audio.read())

    return converted_audio

def speech_to_text_google(namefile_wav):
    """
        распознование wav файла в текст используя гугл (почему-то нормально не работает)
    """
    audio_source=None
    audio = None
    with open(namefile_wav,'rb') as out: 
        audio_source = io.BytesIO(out.read())
    # Initialize a new recognizer with the audio in memory as source
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_source) as source:
        audio = recognizer.record(source) # read the entire audio file
    print(audio)

    audio_output = ""
    # recognize speech using Google Speech Recognition
    try:
        audio_output = recognizer.recognize_google(audio)
    except KeyError:                                    # the API key didn't work
        print("Invalid API key or quota maxed out")
    except LookupError:                                 # speech is unintelligible
        print("Could not understand audio")    
    print("[{0}] Google Speech Recognition: ".format(audio_output))
    # Check if we got harder audio captcha
           
    return audio_output


def speech_to_text_wit_ai(namefile_wav):
    """
        распознование wav файла в текст используя wit.ai (распознает, но не очень)
    """
    audio_source=None
    audio = None
    with open(namefile_wav,'rb') as out: 
        audio_source = io.BytesIO(out.read())
    # Initialize a new recognizer with the audio in memory as source
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_source) as source:
        audio = recognizer.record(source) # read the entire audio file
    print(audio)
    audio_output = ""
    # recognize speech using Wit.ai
    WIT_AI_KEY = "V4ARGX6BTUHTTC5H6XYHCGCSWFD2QPQC"  # Wit.ai keys are 32-character uppercase alphanumeric strings
    try:
        audio_output = recognizer.recognize_wit(audio, key=WIT_AI_KEY)
    except sr.UnknownValueError:
        print("Wit.ai could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit.ai service; {0}".format(e))
    return audio_output


def save_link_to_wav(url, namefile_wav = "tst.wav"):
    """
        сохранение урл в звуковой файл формата wav
    """
    #url = 'https://www.google.com/recaptcha/api2/payload/audio.mp3?c=03AJpayVHL88o5_t_Ngh-JEdiB5gTimwLs7Q2FJhTHw7Dh-Nq_6w84L4HT0FUFmlcRj74Sp8DE-DwUf9WJDVLIj5sYncJeKr1e6ixkstK6yHTj4id9FS13maCV30t4nZWoQSLvnDv4Oft_Zju5PqdaqzMFwSgklCoJl1tVYxTQZJ_0hmDdqfgTBYVigaEmb7e8cJnIzmh3dZ5cJs4y2nWzhU9Fy0yv_7o9DBEW2SL8NLWeZj41YcdshYJEmUXRgItouLfMRXs4ZH3YJVaVh7iqZWOIfJRS9ycxMLMas7boNxp2cpVSXMN5WKSQl67KJhHouebdbRrejvNvHNy-ng6d5dx99PNLBgDWTaQ-gbPqMu3DczzJ3xIZ7hxPRivTfN0YroAvF1cXvePui14Z_f4pVbWI0aFuKuzy2xMLKH33_UnIsbvkr-betC1H6sEZTDKOoQcA0dDUFjJZZIJbfoBaZuc_lj9iaxWguW9nHFAe-UNi58F_O93xAwOE7AoZB0CHD00gpbVldQNcOuFnu3ihaFbkGsLspHyezqSX7NJ_P3UlsPa3gyP890aGXvqV2Jd1gcl5aSg2DbGN9r7PhtWojJPTGVyfzZTBLHUy7C5z4i_2ZG3p1tvKcJAHnFqRBLNGpooAx9pnv8w1REqFkJrzVy-XoUyJogDnFwh9Ec1QxS2iH2UDLO3-ajTkGhgXgxoubaFhX_6vy1jEJ0XjbfbcZb90N13AM_l5onDzXk00wLHaihbaJM53rWcpCii8O-MsBz8u-svlHoLrB4tQn70QrQDsX1swz18YHbMhpVpdyRBTM9L-50cr_-ltJTomoBgZQqs2EeSB5Vixno2B-VgFV_GBK52XtpnfanSGUK0yLNtr6mkAU8TjkfKYcPxUBZsqGkitJM7xeabtdFn_1TM9LDhavAMus5hvRXu0fmiT24cWyOaSV7lHjMhYDrKx1wN-dKo90mQ4hoeLo_iqX84mTyuirfr6AL2LnQ_sWbiDBajDfR43dLlv-WzD1vHx5X_pulWt643eBuwmpzC6grvwqQrQcv9JebH1co5xrdHrOa0psyWCODGe2QNpyRozFLi8tP19ZDOAZnjhYOZAvk-pgRG0GrUxbMmyv0Cc6zO0btTdQJUw0e4plI8iD-4jJqIm83zyRxHVXBI0DfuzVnu2G8j2OA5Vj1KEvw3hV4yZmSprlaEOmMDMv_L_BZMzsBadmSfHU7LJ4siVRrazHmL3O5-txQsqKlUOGowikDA74XfitB751UxiP1DbVSXWBYhly3yWuqWazcEyikGpgqO714WV6UiWIJUxnw&k=6LfYD0YUAAAAAMznM1CHezCFL34jLmCgfYGWL3oT'
    save_audio_from_url(url,"sound2.mp3")
    time.sleep(1)
    convert_mp3_to_wav("sound2.mp3", namefile_wav)



if __name__=="__main__":
    #api_yandex_speechkit_cloud ="9ed6a4fb-edbe-49d5-9f62-a3665e93bf59"
    #namefile_wav = "audio_cap.wav"
    namefile_wav = "tst.wav"

    # Send the audio to Google Speech Recognition API and get the output
    #audio_output = speech_to_text_google(namefile_wav)
    #audio_output = speech_to_text_yandex(filename=namefile_wav, key=api_yandex_speechkit_cloud)
    audio_output = speech_to_text_wit_ai(namefile_wav)
    print(audio_output)
