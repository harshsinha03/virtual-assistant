import pyttsx3 # pyttsx3 is a library that coverts text to speech
import datetime # to tell date and time
import speech_recognition as sr
import wikipedia
import webbrowser




engine = pyttsx3.init('sapi5') # SAPI5 is used for voice recognition 

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetings():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour <= 12):
        speak("Good Morning!")
    elif hour >= 12 and hour < 17:
        speak("Good afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Ashish how may i assist you?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.pause_threshold = 0.8
        audio = recognizer.listen(source)

    try:
        print('Recognizing....')
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said:{query}")

    except Exception:
    
        print("Please, say it again")
        return "None"
    
    return query



if __name__ == "__main__":
    greetings()
    if 1:
        query = take_command().lower()
        
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            speak(result)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"the time is {Time}")



        


