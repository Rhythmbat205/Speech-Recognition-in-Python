import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import subprocess 
import time
import random
import ctypes



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your assistant Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

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
       
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email_id', 'your_password')
    server.sendmail('your_email_id', to, content)
    server.close()

def note(text):
    date =datetime.datetime.now()
    file_name = str(date).replace(":","-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    
    subprocess.Popen(["notepad.exe", file_name])

Note_strs = ["make a note", "write this"]   
Wake = "hey system"

email = {
    'friend1':'friend1@gmail.com',
    'friend2':'friend2@gmail.com',
    'friend3':'friend3@gmail.com',
    'friend4':'friend4@gmail.com'
    }


Words = ['tree', 'salad', 'corona', 'watch','laptop','phone']
def game():
    speak("Well, I have a game for you known as ,Word Guess!!, I'll think about a word from a list and you have to guess which word it is. You will be given 3 chances. so be ready")
    comp = random.choice(Words)
    speak("I have been thinking about a word, Guess which one")
    print(Words)
    
    for i in range(3,0,-1):
        speak("You have {} chances left".format(i))
        user = takeCommand().lower()
        #print(comp)
        if user == comp:
            speak("Yeah thats right!!")
            break
        else:
            speak("Try Again")
            

def reciever(name):
    for key, value in email.items():
        if name == key:
            return value

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

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'open geeks for geeks' in query:
            webbrowser.open("geeksforgeeks.org") 
        
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        
        elif 'play music' in query:
            music_dir = 'D:\hard disk\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            speak("Whom do you want to send email?")
            name = takeCommand().lower()
            to = reciever(name)
            print(to)


            try:
                speak("What should I say?")
                content = takeCommand().lower()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")    

        elif 'lock' in query:
            ctypes.windll.user32.LockWorkStation()
        
        elif 'note' in query:
            speak("what would you like to write down?")
            note_text = takeCommand().lower()
            note(note_text)
            speak("I've done that for you")


        elif "thank you" in query:
            speak("its my pleasure!, sir")
        
        elif 'create folder' in query:
            try:
                speak("What name do you want to give to you folder?")
                folder = takeCommand().lower()
                parent_dir = "D:\Assistant"
                path = os.path.join(parent_dir, folder)
                os.makedirs(path)
                speak("Directory '% s' created" %folder)
            except Exception as e:
                print(e)
        
        elif 'set a reminder' in query:
            speak("What shall I remind you about?")
            rem = takeCommand().lower()
            speak("In how many minutes?")
            local_time = float(takeCommand().lower())
            local_time = local_time*60
            time.sleep(local_time)
            speak(rem)

        
        elif 'game' in query:
            game()
     
        else:
            speak("You may have to update me for this instruction,sir")

        
           
            
           

        
