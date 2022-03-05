import speech_recognition as sr

mic = sr.Recognizer()

with sr.Microphone() as source:
    mic.adjust_for_ambient_noise(source)

    print('Diga alguma coisa...')

    audio = mic.listen(source)

    try:
        frase = mic.recognize_google(audio, language='pt-BR')
        print('Você disse: ' + frase)
    except sr.UnknownValueError:
        print('Desculpe, eu não entendi!')
