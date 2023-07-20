import speech_recognition as sr
import pyttsx3 
from langdetect import detect
from googletrans import Translator

#create a recognizer object, a translator object, and a Text-to-Speern object
r=sr.Recognizer() 
translator=Translator(service_urls=['translate.google.com'])
tts=pyttsx3.init()

while True:
    choice=input("Select the procedure\n1-English to Any Language\n2-Any language to English\n")

    # use the default microphone as the audio source 
    with sr.Microphone() as source:
        print("Speak something...")
        #adjust the ambient noise level
        r.adjust_for_ambient_noise (source)
        #listen for audio input from the user 
        audio= r.listen(source)
    try:
        if (choice==1):
            #recognize speech using Google Speech Recognition
            text = r.recognize_google(audio) 
            input_language = detect(text)
            print("You said: ",text)
            #translate speech to English if detected language is spanish
            #if input_language =="es": 
            language=input("In which language you want to translate?")
            translation=translator.translate(text, dest=language)
            print(f"Translated to English: {translation.text}")
            #speak the translated text 
            tts.say(translation.text)
            tts.runAndWait()
        else:
            #recognize speech using Google Speech Recognition
            text = r.recognize_google(audio) 
            input_language = detect(text)
            print("You said: ",text)
            translation=translator.translate(text, dest='en')
            print(f"Translated to English: {translation.text}")
            #speak the translated text 
            tts.say(translation.text)
            tts.runAndWait() 
    except sr.UnknownValueError:
        print("Google speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google sppech recognition service; {e}")