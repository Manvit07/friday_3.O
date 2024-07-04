import pyttsx3
import speech_recognition as sr
import pyautogui
import time
import datetime

# Body of Friday
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 225)

# Speaking function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wish Me function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning BOSS!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon BOSS!")
    else:
        speak("Good Evening BOSS!")
    speak("Friday in your service. How can I help you today?")

# Take Command function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except sr.UnknownValueError:
        print('Sorry, I did not understand that. Please say that again.')
        speak('Sorry, I did not understand that. Please say that again.')
        return "None"
    
    return query.lower()

# Open Chrome function
def open_chrome():
    pyautogui.hotkey("win")
    time.sleep(1)
    pyautogui.write('chrome')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

# Maximize Window function
def maxi():
    pyautogui.hotkey('alt', 'space')
    time.sleep(1)
    pyautogui.press('x')

# Minimize Window function
def mini():
    pyautogui.hotkey('alt', 'space')
    time.sleep(1)
    pyautogui.press('n')

# Google Search function
def g_search(query):
    pyautogui.hotkey('ctrl','t')
    time.sleep(1)
    query = query.replace("friday","").replace("search on google", "")
    pyautogui.hotkey('alt', 'd')
    pyautogui.write(f"{query}", 0.1)
    time.sleep(0.5)
    pyautogui.press('enter')

# YouTube Search function
def y_search(query):
    query = query.replace("search on youtube", "")
    pyautogui.hotkey('alt', 'd')
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')                   
    time.sleep(1)
    pyautogui.write(f"{query}", 0.1)
    pyautogui.press('enter')

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()
        
        if "open chrome" in query:
            open_chrome()
            speak("Anything else I can help you with, sir?")
            
        elif 'search on google' in query:
            g_search(query)
            speak("Anything else I can help you with, sir?")
            
        elif 'search on youtube' in query:
            y_search(query)
            speak("Anything else I can help you with, sir?")
        
        elif 'maximize' in query:
            maxi()
            speak("Anything else I can help you with, sir?")
            
        elif 'minimize' in query:
            mini()
            speak("Anything else I can help you with, sir?")
            
        elif 'open new window' in query:
            pyautogui.hotkey('ctrl','n')
            speak("Anything else I can help you with, sir?")    
            
        elif 'close the window' in query:
            pyautogui.hotkey('ctrl','shift', 'w')
            speak("Anything else I can help you with, sir?")
            
        elif 'open a new tab' in query:
            pyautogui.hotkey('ctrl','t')
            speak("Anything else I can help you with, sir?")
                    
        elif 'close this tab' or 'close tab' in query:
            pyautogui.hotkey("ctrl","w")
            speak("Anything else I can help you with, sir?")
            
        

