import json
import time
from time import sleep

import speech_recognition as sr
import re
import pyttsx3
import os
import pygame
import pyaudio
from vosk import Model, KaldiRecognizer

escutando = True  # Variável pra identificar primeiro acesso do looping
# --------- Inicialização dos processos -----------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[2].id)
model = Model('model')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()
pygame.init()
pygame.mixer.music.load('escutando.mp3')
# -------------------------------------------------


# Função da fala do assitente
def falar(frase):
    engine.say(frase)
    engine.runAndWait()


def escutar():
    pygame.mixer.music.play()
    rec = KaldiRecognizer(model, 16000)
    inicio = time.perf_counter()
    frase = ''

    while time.perf_counter() - inicio < 4:
        data = stream.read(2048)

        if len(data) == 0:
            break

        if rec.AcceptWaveform(data):
            resultado = rec.Result()
            resultado = json.loads(resultado)

            if resultado is not None:
                frase = resultado['text']

    print('Saiu')
    return frase


while True:

    if escutando:
        frase = escutar()
        print(frase)
        if re.search(r'\b' + 'ajudar' + r'\b', format(frase)):
            falar('Desculpe não posso te ajudar no momento, ainda estou em desenvolvimento')

    while True:
        data = stream.read(2048)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            resultado = rec.Result()
            resultado = json.loads(resultado)

            if resultado is not None:
                frase = resultado['text']
                print(frase)

                if 'bruno' in frase:
                    break

    # try:
    #     if re.search(r'\b' + 'meu nome é' + r'\b', format(frase)):
    #         t = re.search('meu nome é (.*)', format(frase))
    #         nome_usuario = t.group(1)
    #         engine.say('Olá ' + nome_usuario + 'é um prazer te conhecer')
    #         engine.runAndWait()
    #         break
    #
    #     if re.search(r'\b' + 'abrir o navegador' + r'\b', format(frase)):
    #         engine.say('Ok... Abrindo o navegador')
    #         engine.runAndWait()
    #         os.startfile(r"C:\Users\bruno\AppData\Local\Programs\Opera\launcher.exe")
    #         break
    #     # ---------------------------------------------------------------------------------------
