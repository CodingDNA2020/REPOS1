import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("afternoon")
    else:
        speak("good evening")
    
    speak("i am jarvis sir. how may i help you ")

def takecommand():
    #it takes microphone input from the user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("Recognizing")
        query=r.recognize_google(audio,language='en-in')
        print("user said",query)
        
    except Exception as e:
        print(e)
        print("say again please...")
        return "none"
    return query

if __name__== "__main__" :  
    wishMe()
    #while True:
    if 1:    
        query=takecommand().lower()
    #logic for executing task based on query
        if 'wikipedia' in query:
            speak('serching wikipedia...')
            query=query.replace('wikipedia', '')
            result=wikipedia.summary(query, sentences=4)
            speak("according to wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("youtube.com") 
          
        elif 'open facebook' in query:
            webbrowser.open("youtube.com")
            
        elif 'play music' in query:
            music_dir='G:\\songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[6]))
         
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"sir,the time is{strTime}")
           
        elif 'open code' in query:
             codepath="C:\\ProgramData\\Anaconda3\\pythonw.exe C:\\ProgramData\\Anaconda3\\cwp.py C:\\ProgramData\\Anaconda3 C:\\ProgramData\\Anaconda3\\pythonw.exe C:\\ProgramData\\Anaconda3\\Scripts\\anaconda-navigator-script.py"
             os.startfile(codepath)
                                    
            
            
    