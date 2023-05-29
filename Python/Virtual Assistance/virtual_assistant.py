import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import time

class Assistant:
    def __init__(self, name='Whale'):
        self.name = name
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0')
        self.recognizer = sr.Recognizer()

    def speak(self, message):
        self.engine.say(message)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            self.recognizer.pause_threshold = 0.8
            try:
                self.speak("I'm listening...")
                audio = self.recognizer.listen(source)
                request = self.recognizer.recognize_google(audio, language="en-gb")
                print("You said " + request)
                return request.lower()
            except sr.UnknownValueError:
                self.speak("Ups! I didn't understand audio")
                return "I am still waiting"
            except sr.RequestError:
                self.speak("Ups! there is no service")
                return "I am still waiting"
            except:
                self.speak("Ups! something went wrong")
                return "I am still waiting"



    def open_youtube(self):
        self.speak('Sure, I am opening youtube')
        webbrowser.open('https://www.youtube.com')

    def open_browser(self):
        self.speak ('Of course, I am on it')
        webbrowser.open('https://www.google.com')

    def tell_day(self):
        day = datetime.date.today()
        week_day = day.weekday()
        calendar = {0: 'Monday',
                    1: 'Tuesday',
                    2: 'Wednesday',
                    3: 'Thursday',
                    4: 'Friday',
                    5: 'Saturday',
                    6: 'Sunday'}
        self.speak(f'Today is {calendar[week_day]}')

    def tell_time(self):
        time = datetime.datetime.now()
        time_str = f'At this moment it is {time.hour} hours and {time.minute} minutes'
        self.speak(time_str)

    def wikipedia_search(self, command):
        self.speak('I am looking for it')
        request = command.replace('do a wikipedia search for', '')
        answer = wikipedia.summary(request, sentences=1)
        self.speak('according to wikipedia: ')
        self.speak(answer)

    def internet_search(self, command):
        self.speak('of course, right now')
        request = command.replace('search the internet for', '')
        pywhatkit.search(request)
        self.speak('this is what i found')

    def play_music(self, command):
        self.speak('oh, what a great idea! I´ll play it right now')
        pywhatkit.playonyt(command)

    def tell_joke(self):
        self.speak(pyjokes.get_joke())

    def stock_price(self, command):
        share = command.split()[-2].strip()
        portfolio = {'apple': 'APPL',
                     'amazon': 'AMZN',
                     'google': 'GOOGL'}
        try:
            searched_stock = portfolio[share]
            searched_stock = yf.Ticker(searched_stock)
            price = searched_stock.info['regularMarketPrice']
            self.speak(f'I found it! The price of {share} is {price}')
        except:
            self.speak('I am sorry, but I didn´t find it')

    def start(self):
        self.speak(f'Hello I am {self.name}. How can I help you?')
        while True:
            time.sleep(1)
            request = self.listen()
            if 'open youtube' in request:
                self.open_youtube()
            elif 'open browser' in request:
                self.open_browser()
            elif 'what day is today' in request:
                self.tell_day()
            elif 'what time it is' in request:
                self.tell_time()
            elif 'do a wikipedia search for' in request:
                self.wikipedia_search(request)
            elif 'search the internet for' in request:
                self.internet_search(request)
            elif 'play' in request:
                self.play_music(request)
            elif 'joke' in request:
                self.tell_joke()
            elif 'stock price' in request:
                self.stock_price(request)
            elif 'goodbye' in request:
                self.speak('I am going to rest. Let me know if you need anything')
                break


assistant = Assistant()
assistant.start()
