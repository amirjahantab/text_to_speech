import pyttsx3

engine = pyttsx3.init()

text = str(input("enter your text"))

engine.say(text)

engine.runAndWait()
