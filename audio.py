import speech_recognition as sr

def recognize_speech():
    recognizer  = sr.Recognizer()

    with sr.Microphone() as source:
        print('Слушаю...')

        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        audio = recognizer.listen(source,timeout=3,phrase_time_limit=5)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU") # Распознает текст
        return text 
    except sr.UnknownValueError:
        return "Не удалось распознать речь"
    except sr.RequestError:
        return "Ошибка сервиса распознавания"