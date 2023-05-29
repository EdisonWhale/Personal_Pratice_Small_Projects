from contextlib import contextmanager
from ctypes import *
import time
import pygame
import google.cloud.texttospeech as tts
from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha
import keyboard

import openai

# Load credentials
import os
from dotenv import load_dotenv
load_dotenv()

# Google TTS

# Mute ALSA errors...

ERROR_HANDLER_FUNC = CFUNCTYPE(
    None, c_char_p, c_int, c_char_p, c_int, c_char_p)


def py_error_handler(filename, line, function, err, fmt):
    pass


c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)


@contextmanager
def noalsaerr():
    try:
        asound = cdll.LoadLibrary('libasound.so')
        asound.snd_lib_error_set_handler(c_error_handler)
        yield
        asound.snd_lib_error_set_handler(None)
    except:
        yield
        print('')


### PARAMETERS ###
activationWords = ['computer', 'calcutron', 'shodan', 'showdown']
tts_type = 'local'  # google or local

# Local speech engine initialisation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 = male, 1 = female

# Google TTS client


def google_text_to_wav(voice_name: str, text: str):
    language_code = "-".join(voice_name.split("-")[:2])

    # Set the text input to be synthesized
    text_input = tts.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the voice name
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )

    # Select the type of audio file you want returned
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input, voice=voice_params, audio_config=audio_config
    )

    return response.audio_content


# Configure browser
# Set the path
firefox_path = r"usr/bin/firefox"
# Register the browser
webbrowser.register('firefox', None,
                    webbrowser.BackgroundBrowser(firefox_path))

# Wolfram Alpha client
appId = '5R49J7-J888YX9J2V'
wolframClient = wolframalpha.Client(appId)


def speak(text, rate=120):
    print(f'Speaking: {text}')
    time.sleep(0.3)
    try:
        if tts_type == 'local':
            engine.setProperty('rate', rate)
            engine.say(text, 'txt')
            engine.runAndWait()
        if tts_type == 'google':
            speech = google_text_to_wav('en-US-News-K', text)
            pygame.mixer.init(frequency=12000, buffer=512)
            speech_sound = pygame.mixer.Sound(speech)
            speech_length = int(
                math.ceil(pygame.mixer.Sound.get_length(speech_sound)))
            speech_sound.play()
            time.sleep(speech_length)
            pygame.mixer.quit()

    # The standard keyboard interrupt is Ctrl+C. This interrupts the Google speech synthesis.
    except KeyboardInterrupt:
        try:
            if tts_type == 'google':
                pygame.mixer.quit()
        except:
            pass
        return


def parseCommand():
    with noalsaerr():
        listener = sr.Recognizer()
        print('Listening for a command')

        with sr.Microphone() as source:
            listener.pause_threshold = 2
            input_speech = listener.listen(source)

        try:
            print('Recognizing speech...')
            query = listener.recognize_google(input_speech, language='en_gb')
            print(f'The input speech was: {query}')

        except Exception as exception:
            print('I did not quite catch that')
            print(exception)

            return 'None'

        return query


def search_wikipedia(keyword=''):
    searchResults = wikipedia.search(keyword)
    if not searchResults:
        return 'No result received'
    try:
        wikiPage = wikipedia.page(searchResults[0])
    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.options[0])
    print(wikiPage.title)
    wikiSummary = str(wikiPage.summary)
    return wikiSummary


def listOrDict(var):
    if isinstance(var, list):
        return var[0]['plaintext']
    else:
        return var['plaintext']


def search_wolframalpha(keyword=''):
    response = wolframClient.query(keyword)

    # @success: Wolfram Alpha was able to resolve the query
    # @numpods: Number of results returned
    # pod: List of results. This can also contain subpods

    # Query not resolved
    if response['@success'] == 'false':
        speak('I could not compute')
    # Query resolved
    else:
        result = ''
        # Question
        pod0 = response['pod'][0]
        # May contain answer (Has highest confidence value)
        # if it's primary or has the title of result or definition, then it's the official result
        pod1 = response['pod'][1]
        if (('result') in pod1['@title'].lower()) or (pod1.get('@primary', 'false') == 'true') or ('definition' in pod1['@title'].lower()):
            # Get the result
            result = listOrDict(pod1['subpod'])
            # Remove bracketed section
            return result.split('(')[0]
        else:
            # Get the interpretation from pod0
            question = listOrDict(pod0['subpod'])
            # Remove bracketed section
            question = question.split('(')[0]
            # Could search wiki instead here?
            return question


def query_openai(prompt=""):
    try:
        openai.organization = os.environ['OPENAI_ORG']
        openai.api_key = os.environ['OPENAI_API_KEY']

        print(f'Organization: {openai.organization}')
        print(f'API key: {openai.api_key}')
        # Temperature is a measure of randomness
        # Max_tokens is the number of tokens to generate
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.3,
            max_tokens=80,

        )

        return response.choices[0].text
    except Exception as e:
        print(f"Error while querying OpenAI: {e}")
        return None


# Main loop
if __name__ == '__main__':
    speak('All systems nominal.', 120)

    while True:
        # Parse as a list
        # query = 'computer say hello'.split()
        command = parseCommand()
        if command is None:
            continue  # If the command is None, skip the rest of the loop
        query = command.lower().split()

        if query[0] in activationWords and len(query) > 1:
            query.pop(0)

            # Set commands
            if query[0] == 'say':
                if 'hello' in query:
                    speak('Greetings, all!')
                else:
                    query.pop(0)  # Remove 'say'
                    speech = ' '.join(query)
                    speak(speech)

            # Query OpenAI
            if query[0] == 'Friday':
                query.pop(0)  # Remove 'Friday'
                query = ' '.join(query)
                print("About to call OpenAI API with query:", query)  # 添加的打印语句
                result = query_openai(query)
                print("Result from OpenAI API:", result)  # 添加的打印语句
                if result:
                    # Add print statement here
                    print(f'OpenAI result: {result}')
                    speak(result)
                else:
                    print("Failed to get result from OpenAI")
                    speak("Sorry, I couldn't fetch the information right now.")

            # Navigation
            if query[0] == 'go' and query[1] == 'to':
                speak('Opening... ')
                # Assume the structure is activation word + go to, so let's remove the next two words
                query = ' '.join(query[2:])
                webbrowser.get('chrome').open_new(query)

            # Wikipedia
            if query[0] == 'wikipedia':
                query = ' '.join(query[1:])
                speak('Querying the universal databank')
                time.sleep(2)
                result = search_wikipedia(query)
                # Add print statement here
                print(f'Wikipedia result: {result}')
                speak(result)

            # Wolfram Alpha
            if query[0] == 'calculate' or query[0] == 'calculate':
                query = ' '.join(query[1:])
                try:
                    result = search_wolframalpha(query)
                    speak(result)
                except:
                    speak('Unable to compute')

            # Note taking
            if query[0] == 'log':
                speak('Ready to record your note')
                newNote = parseCommand().lower()
                now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                with open('note_%s.txt' % now, 'w') as newFile:
                    newFile.write(now)
                    newFile.write(' ')
                    newFile.write(newNote)
                speak('Note written')

            if query[0] == 'exit':
                speak('Goodbye')
                break
