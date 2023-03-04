import pyttsx3 #module used to convert text to audio vise verasa
import datetime
import speech_recognition as sr #which recognise our voice with internet connection
import wikipedia #used to get the search results from wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui#used to access the gui functions
import psutil
import pyjokes
engine = pyttsx3.init()

def speak(audio):#used to convert any text to audio
    engine.say(audio)
    engine.runAndWait()
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The time is now")
    speak(Time)
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("The date is")
    speak(date)
    speak(month)
    speak(year)
def wishme():
    speak("Welcome back....")
    hour=datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning, buddy!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon, buddy!")
    elif hour >=18 and hour<24:
        speak("Good Evening, buddy!")
    else:
        speak("Good Nigth, buddy!")
       
    speak("I am Jarvis....,How can i help you?")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for background noise. One second")
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recongnizing....")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Sorry..I can't get you. Say that again please....")
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()# used to check for the connection for the server
    server.starttls()
    server.login('amarsasierode@gmail.com','Password')
    server.sendmail('amarsasierode@gmail.com',to,content)
    server.close()
def screenshot():
    img=pyautogui.screenshot()
    img.save('C:\\Users\\dell\\Pictures\\Screenshots\\ss.png')
def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at"+usage)
    battery=psutil.sensors_battery()
    speak("Battery is at..")
    speak(battery.percent)
def jokes():
    speak(pyjokes.get_joke())
if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query=query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should i add in that mail?")
                content = takeCommand()
                to = 'sasiamarerode@gmail.com'
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to sent the Email")
        elif 'search in chrome' in query:
            speak("What should i want to search for you?")
            chromepath= 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
            quit()
        elif 'searching chrome' in query:
            speak("What should i want to search for you?")
            chromepath= 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
            quit()
        elif 'logout' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'play song' in query:
            song_dir='C:/Users/dell/Music'
            songs=os.listdir(song_dir)
            os.startfile(os.path.join(song_dir,songs[0]))
            quit()
        elif 'remember that' in query:
            speak("What should i remember?")
            data=takeCommand()
            speak("you said me to remember that"+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember=open('data.txt','r')
            speak("You said me to remember that"+remember.read())
        elif 'screenshot' in query:
            screenshot()
            speak("Doonnee")
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()
        elif 'offline' in query:
            speak("Going Offline")
            quit()
        
        
