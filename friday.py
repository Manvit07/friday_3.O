import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import requests
from bs4 import BeautifulSoup
import pywhatkit as wk
import os
import random
import cv2
import pyautogui
import time
import operator

#-------------------body of friday----------------------------------#
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 225)
#-------------------------------------------------------------------#

#----------------------speaking function----------------------------------#
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#--------------------------------------------------------------------------#

#-------------------------------------wish me fuction----------------------------#
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning BOSS!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon BOSS!")
    else:
        speak("Good Evening BOSS!")
    speak("Friday in your service. How can I help you today?")
#--------------------------------------------------------------------------------#

#-------------------------------------take command--------------------------------#
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
#----------------------------------------------------------------------------------#

#--------------------------play music function-----------------------------------#
def open_youtube():
    speak("which song would you like to listen, sir?")
    qrry = takeCommand().lower()
    wk.playonyt(qrry)
#--------------------------------------------------------------------------------#

#---------------------------time function---------------------------------------#
def get_time():
    return datetime.datetime.now().strftime("%H:%M")
#--------------------------------------------------------------------------------#

#-------------------------------day function-------------------------------------#
def get_day():
    return datetime.datetime.now().strftime("%A")
#--------------------------------------------------------------------------------#

#-------------------------------date funtion-------------------------------------#
def get_date():
    return datetime.datetime.now().strftime('%d %B %Y')
#-------------------------------------------------------------------------------#  

#-------------------------------OK google function------------------------------#
def get_google_summary(query):
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    summary = soup.find('span', {'class': 'aCOpRe'})
    if summary:
        return summary.text
    else:
        return "I could not find a summary for that topic."

def ok_google():  
    speak("What should I search for you, sir?")
    qry = takeCommand().lower()
    if qry != "None":
        summary = get_google_summary(qry)
        speak(summary)
        webbrowser.open(f"https://www.google.com/search?q={qry}")
        speak("These are some of the most viewed sites.")
#-------------------------------------------------------------------------------#

#-----------------------close broewer-----------------------------------------#
def close_brow():
    os.system("taskkill /f /im chrome.exe")
#-----------------------------------------------------------------------------#

#----------------------------close edge------------------------------------------#
def close_edge():
    os.system("taskkill /f /im msedge.exe")
#---------------------------------------------------------------------------------#

#----------------------------------opent paint function------------------------#
def open_paint():
    npath = "C:\\Program Files\\WindowsApps\\Microsoft.Paint_11.2404.1020.0_x64__8wekyb3d8bbwe\\PaintApp\\mspaint.exe"
    os.startfile(npath)
#------------------------------------------------------------------------------#

#--------------------------close paint function ------------------------------#
def close_paint():
    os.system("taskkill /f /im mspaint.exe")
#-----------------------------------------------------------------------------#

#--------------------------open notepad-----------------------------------------------#
def open_notepad():
    npath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2405.13.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
    os.startfile(npath)
#----------------------------------------------------------------------------------------#

#---------------------------------------------close notepad---------------------------------#
def close_notepad():
    os.system("taskkill /f /im Notepad.exe")
#-------------------------------------------------------------------------------------------#

#-----------------------------------------------open cmd-------------------------------------------#
def open_cmd():
    os.system("start cmd")
#------------------------------------------------------------------------------------------------#

#------------------------------------------close cmd--------------------------------------------#
def close_cmd():
    os.system("taskkill /f /im cmd.exe")
#-----------------------------------------------------------------------------------------------#

#----------------------------------------play music---------------------------------------------#
def play_music():
    music_dir = "D:\\music"  
    if os.path.exists(music_dir):
                    songs = os.listdir(music_dir)
                    song_to_play = random.choice(songs)
                    os.startfile(os.path.join(music_dir, song_to_play))
#-----------------------------------------------------------------------------------------------#      

#------------------------------------close music-----------------------------------------------#
def close_music():
    os.system("taskkill /f /im wmplayer.exe")
#-----------------------------------------------------------------------------------------------#              

#---------------------------------------------------open camera---------------------------------#

def open_camera():
    cap = cv2.VideoCapture(0)  # Initialize the camera (0 is typically the default camera)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()  # Capture frame-by-frame
        if not ret:
            print("Error: Failed to capture frame.")
            break

        cv2.imshow("webcam", frame)  # Display the resulting frame

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit loop if 'q' is pressed
            break

    cap.release()  # Release the capture
    cv2.destroyAllWindows()  # Close all OpenCV windows

#-----------------------------------------------------------------------------------------------#

#---------------------------------------take screenshot-----------------------------------------#
def take_screenshot():
    speak("Tell me a name for the file")
    name = takeCommand().lower()
    time.sleep(3)
    screenshot_directory = "D:\\screenshots" 
    if not os.path.exists(screenshot_directory):
        os.makedirs(screenshot_directory) 
        file_path = os.path.join(screenshot_directory, f"{name}.png")
        img = pyautogui.screenshot()
        img.save(file_path)
        speak(f"Screenshot saved as {file_path}")
#----------------------------------------------------------------------------------------------#

#---------------------------------------------start_cal-----------------------------------------#
def start_cal():
    pyautogui.press('win')
    time.sleep(0.45)
    pyautogui.typewrite('calcul',0.1)
    time.sleep(0.45)
    pyautogui.press("enter")                              
#------------------------------------------------------------------------------------------------#

#---------------------------------close cal--------------------------------------------------------#
def close_cal():
    time.sleep(1)
    pyautogui.hotkey('alt',"F4")
#--------------------------------------------------------------------------------------------------#

#---------------------------------------------ip add --------------------------------------------#
def ip_add():
    speak("checking")
    try:
                    ipadd = requests.get("https://api.ipify.org").text
                    print(ipadd)
                    speak("your ip address is")
                    speak(ipadd)
    except Exception as e:
                    speak("network is weak, lease try again some time later")
#-----------------------------------------------------------------------------------------------#

#------------------------------------take note--------------------------------------------------#
def take_note():
    pyautogui.hotkey("win")
    time. sleep (1)
    pyautogui.write( 'notepad')
    time.sleep (1)
    pyautogui.press('enter')
    time.sleep (1)
    speak("ready to type sir...!")
    quy = takeCommand().lower()
    quy = quy.replace("type","")
    pyautogui.typewrite(f"{quy}", 0.1)
#--------------------------------------------------------------------------------------------------#

#----------------------------------sticky note----------------------------------------------------#
def sticky_note():
    pyautogui.hotkey("win")
    time. sleep (1)
    pyautogui.write('stickey')
    time.sleep (1)
    pyautogui.press('enter')
    time.sleep (1)
    speak("ready to type sir...!")
    quy = takeCommand().lower()
    quy = quy.replace("type","")
    pyautogui.typewrite(f"{quy}", 0.1)
#-----------------------------------------------------------------------------------------------------#

#--------------------------------------vloume up------------------------------------------------------#
def volume_up():
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
#---------------------------------------------------------------------------------------------------------#

#---------------------------vloume down------------------------------#
def volume_down():
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
#------------------------------------------------------------------------#

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            wishMe()
        
        while True:
            query = takeCommand()
        
            if query != "None":
                print(f"Recognized query: {query}")
              
            if "time" in query:
                speak(f"Sir, the time is {get_time()}")
                speak("Anything else I can help you with, sir?")

            elif 'date' in query:
                speak(f"Sir, today's date is {get_date()}")
                speak("Anything else I can help you with, sir?")
        
            elif 'week day' in query:
                speak(f"Sir, today is {get_day()}")
                speak("Anything else I can help you with, sir?")
                
            if 'play some music'in query:
                open_youtube()
                speak("Anything else I can help you with, sir?")
                
            elif 'search on youtube' in query:
                query = query.replace("friday","").replace("search on youtube", "").strip()
                webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
                speak("Anything else I can help you with, sir?")
                
            elif 'search on google' in query:
                query = query.replace("friday","").replace('search on google',"").strip()
                webbrowser.open(f"https://www.google.com/search?q={query}")
                speak("Anything else I can help you with, sir?")
                
            elif 'open google' in query or 'open the google' in query:
                ok_google()
                speak("Anything else I can help you with, sir?")
                
            elif 'close browser tab' in query or 'close the browser tab' in query:
                close_brow()
                speak("Anything else I can help you with, sir?")
                
            elif 'close microsoft edge' in query or 'close the microsoft edge' in query:
                close_edge()
                speak("Anything else I can help you with, sir?")
                
            elif 'open paint' in query or 'open the paint' in query:
                open_paint()
                speak("Anything else I can help you with, sir?")
                
            elif 'close paint' in query or 'close the paint' in query:
                close_paint()
                speak("Anything else I can help you with, sir?")
                
            elif 'open notepad' in query or 'open the notepad' in query:
                open_notepad()
                speak("Anything else I can help you with, sir?")
                
            elif 'close notepad' in query or 'close the notepad' in query:
                close_notepad()
                speak("Anything else I can help you with, sir?")
                
            elif any(keyword in query for keyword in ["open command prompt", "open cmd", "open cmd command prompt", "open the command prompt", "open the cmd", "open the cmd command prompt"]):
                open_cmd()
                speak("Anything else I can help you with, sir?")
                
            elif any(keyword in query for keyword in ["close command prompt", "close cmd", "close cmd command prompt", "close the command prompt", "close the cmd", "close the cmd command prompt"]):
                close_cmd()
                speak("Anything else I can help you with, sir?")

            elif "shut down the laptop" in query:  
                os.system("shutdown /s /t 5")

            elif "restart the laptop" in query: 
                os.system("shutdown /r/t 5")

            elif "lock the laptop" in query: 
                os.system("rund1132.exe powrprof.dll, SetSuspendState 0,1,0")

            elif "hibernate the system" in query: 
                os.system("rund1132.exe powrprof.dll, SetSuspendState 0,1,0")
                
            elif "open camera" in query:
                open_camera()
                speak("Anything else I can help you with, sir?")
                
            elif "take a screenshot" in query:
                take_screenshot()
                speak("Anything else I can help you with, sir?")
            
            elif "close calculator" or "close the calculator" in query:
                close_cal()
                speak("Anything else I can help you with, sir?")
                
            elif "my ip address" in query:
                ip_add()
                speak("Anything else I can help you with, sir?")
                    
            elif "take a note" in query:
                take_note()
                speak("Anything else I can help you with, sir?")
                    
            elif "stickey notes" in query:
                sticky_note()
                speak("Anything else I can help you with, sir?")
                    
            elif 'increase the volume' in query: 
                volume_up()      
                speak("Anything else I can help you with, sir?")
                
            elif "volume down" in query:
                speak("OK sir, reduceing volume by 20")
                volume_down()
                speak("Anything else I can help you with, sir?")
                
            elif any(keyword in query for keyword in ["close the program", "shut down", "sleep","stop"]):
                speak("OK sir, with your permission...")
                speak("Have a nice day sir!")
                break
                
            elif "start calculator" in query:
                start_cal()
                speak("Anything else I can help you with, sir?")
                                      
        #--------------------------------------------------------#        
            # elif "volume mute" or "volume unmute" in query:
                # pyautogui.press("volumemute")
        #--------------------------------------------------------#

        #------------------------------------playing-downloaded songs---------------------------------------------#               
            # elif "play music" in query:
                # play_music()
                # speak("Anything else I can help you with, sir?")
        #-------------------------------------------------------------------------------------------#

        #-------------------------------------close music--------------------------------------------------------------#
            # elif any(keyword in query for keyword in ["close the music", "close music", "stop the music", "stop music"]):
                # close_music()
                # speak("Anything else I can help you with, sir?")
        #--------------------------------------------------------------------------------------------------------------#