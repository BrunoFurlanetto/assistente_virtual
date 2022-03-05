import speech_recognition as sr
import re
import pyttsx3


mic = sr.Recognizer()

with sr.Microphone() as source:
    engine = pyttsx3.init()
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.luciana')
    mic.adjust_for_ambient_noise(source)

    print('Diga alguma coisa...')

    audio = mic.listen(source)

    try:
        frase = mic.recognize_google(audio, language='pt-BR')

        if re.search(r'\b' + 'ajudar' + r'\b', format(frase)):
            engine.say('Precisa de alguma ajuda?')
            engine.runAndWait()
        elif re.search(r'\b' + 'meu nome é' + r'\b', format(frase)):
            t = re.search('meu nome é (.*)', format(frase))
            nome_usuario = t.group(1)
            engine.say('Olá ' + nome_usuario)
            engine.runAndWait()

    except sr.UnknownValueError:
        print('Desculpe, eu não entendi!')
