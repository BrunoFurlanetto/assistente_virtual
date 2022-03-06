import speech_recognition as sr
import re
import pyttsx3
import os
import pygame

mic = sr.Recognizer()
primeiro = True  # Variável pra identificar primeiro acesso do looping

while True:
    with sr.Microphone() as source:
        # --------- Inicialização dos processos -----------
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty("voice", voices[2].id)
        mic.adjust_for_ambient_noise(source)
        # -------------------------------------------------

        if primeiro:
            pygame.init()
            pygame.mixer.music.load('escutando.mp3')
            pygame.mixer.music.play()
            primeiro = False

        audio = mic.listen(source)

        try:
            frase = mic.recognize_google(audio, language='pt-BR')

            # --------------- Início dos testes para saber o que deverá ser feito -------------------
            if re.search(r'\b' + 'ajudar' + r'\b', format(frase)):
                engine.say('Desculpe não posso te ajudar no momento, ainda estou em desenvolvimento')
                engine.runAndWait()
                break

            if re.search(r'\b' + 'meu nome é' + r'\b', format(frase)):
                t = re.search('meu nome é (.*)', format(frase))
                nome_usuario = t.group(1)
                engine.say('Olá ' + nome_usuario + 'é um prazer te conhecer')
                engine.runAndWait()
                break

            if re.search(r'\b' + 'abrir o navegador' + r'\b', format(frase)):
                engine.say('Ok... Abrindo o navegador')
                engine.runAndWait()
                os.startfile(r'launcher.exe')
                break
            # ---------------------------------------------------------------------------------------

        except sr.UnknownValueError:
            engine.say('Desculpe eu não entendi, pode repetir?')
            engine.runAndWait()
