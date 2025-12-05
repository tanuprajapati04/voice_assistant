import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150) 
        self.engine.setProperty('volume', 0.9) 
        
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)  # 0 for male, 1 for female
        
        self.recognizer = sr.Recognizer()
        
        self.name = "Alexa"
    
    def speak(self, text):
        """Convert text to speech"""
        print(f"Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                command = self.recognizer.recognize_google(audio).lower()
                print(f"You said: {command}")
                return command
            except sr.WaitTimeoutError:
                self.speak("I didn't hear anything. Please try again.")
                return None
            except sr.UnknownValueError:
                self.speak("Sorry, I didn't understand that.")
                return None
            except sr.RequestError:
                self.speak("Network error. Please check your connection.")
                return None
    
    def greet(self):
        hour = datetime.datetime.now().hour
        if hour < 12:
            self.speak("Good morning! How can I help you?")
        elif hour < 18:
            self.speak("Good afternoon! How can I help you?")
        else:
            self.speak("Good evening! How can I help you?")
    
    def get_time(self):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {current_time}")
    
    def get_date(self):
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        self.speak(f"Today is {current_date}")
    
    def search_web(self, query):
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        self.speak(f"Searching for {query} on Google")
    
    def open_website(self, website):
        websites = {
            "youtube": "https://youtube.com",
            "google": "https://google.com",
            "github": "https://github.com",
            "facebook": "https://facebook.com",
            "twitter": "https://twitter.com"
        }
        
        if website in websites:
            webbrowser.open(websites[website])
            self.speak(f"Opening {website}")
        else:
            self.speak(f"I don't know how to open {website}")
    
    def process_command(self, command):
        if command is None:
            return False
        
        if 'exit' in command or 'quit' in command or 'stop' in command:
            self.speak("Goodbye! Have a nice day.")
            return True
        
        elif 'hello' in command or 'hi' in command:
            self.speak("Hello! How can I help you?")
        
        elif 'time' in command:
            self.get_time()
        
    
        elif 'date' in command:
            self.get_date()
        
        elif 'search' in command:
            query = command.replace('search', '').strip()
            if query:
                self.search_web(query)
            else:
                self.speak("What would you like me to search?")
        
        elif 'open' in command:
            for site in ['youtube', 'google', 'github', 'facebook', 'twitter']:
                if site in command:
                    self.open_website(site)
                    break
        
        elif 'your name' in command:
            self.speak(f"My name is {self.name}")
        
            self.show_help()
        
        else:
            self.speak("I'm not sure how to help with that. Try asking for time, date, or search something.")
        
        return False
    
    def show_help(self):
        """Show available commands"""
        help_text = """
        I can help you with:
        - Say 'time' to know current time
        - Say 'date' to know today's date
        - Say 'search' followed by your query to search the web
        - Say 'open' followed by website name (youtube, google, github, etc.)
        - Say 'hello' or 'hi' for greeting
        - Say 'exit', 'quit', or 'stop' to close the assistant
        """
        print(help_text)
        self.speak("Here are the things I can help you with. I've printed them on the screen.")