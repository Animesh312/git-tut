import pyttsx3 #pip install pyttsx3 to import voice engine to python along with this pip install pipwin>>pyaudio
import speech_recognition as sr #pip install speechRecognition
import datetime#to determine date time
import wikipedia #pip install wikipedia
import webbrowser#to fetch into web browser
import os#to get access to all the files in our device
import smtplib#to interface google account with  local apps
import pyjokes#pip install pyjokes

engine = pyttsx3.init('sapi5')#check api for your OS first
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):#to say the  given string or f string
    engine.say(audio)
    engine.runAndWait()


def wishMe():#to wish user according to time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("I am sam. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output
    #try and except to check wether our program is running
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
def joke():
     myjoke=pyjokes.get_joke()
     speak(myjoke)
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)#a kind of try and except wether the api is able to fetch details
    server.ehlo()
    server.starttls()
    server.login('beta.jarvis7@gmail.com','jarvbeta7')#username and password from where email is sent to user
    server.sendmail('atharva.jadhav20@pccoepune.org', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow'in query:
             webbrowser.open("stackoverflow.com") 
           
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\aswan\\AppData\\Local\\Programs\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to atharva' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "athu3108@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")    
        elif 'tell me a joke' in query:
            joke()
        elif 'Thank you' in query:
            speak("Your welcome")
            break    
        
        
