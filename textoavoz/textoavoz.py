#Escriba un programa que permita convertir texto a voz.
import pyttsx3
q = open("archivo.txt")
r = q.read()

voz = pyttsx3.init()

voices = voz.getProperty('voices')
voz.setProperty('voice', voices[2].id)

voz.say(r)
output_file = "audio.mp3"
voz.save_to_file(r, output_file)

voz.runAndWait()

