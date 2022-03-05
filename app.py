import speech_recognition as sr
import re

mic = sr.Recognizer()

with sr.Microphone() as source:
    mic.adjust_for_ambient_noise(source)

    print('Diga alguma coisa...')

    audio = mic.listen(source)

    try:
        frase = mic.recognize_google(audio, language='pt-BR')

        if re.search(r'\b' + 'ajudar' + r'\b', format(frase)):
            print('Algo relacionado a ajuda')
        elif re.search(r'\b' + 'meu nome é' + r'\b', format(frase)):
            t = re.search('meu nome é (.*)', format(frase))
            nome_usuario = t.group(1)
            print('Olá ' + nome_usuario)

    except sr.UnknownValueError:
        print('Desculpe, eu não entendi!')
