# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 18:22:09 2020

@author: Nanthakumaran
"""

import speech_recognition as sr
s=input("Typr the name of the file with its extension")
file=(s)

r=sr.Recognizer()

with sr.AudioFile(file) as source:
    txt=r.record(source)
    
try:
    print(r.recognize_google(txt))
except sr.UnknownValueError:
    print("Can't get it.")
except sr.RequestError:
    print("Can't get it..")