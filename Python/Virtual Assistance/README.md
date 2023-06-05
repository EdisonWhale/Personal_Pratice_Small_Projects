# Personal Voice Assistant

This repository contains a Python-based Personal Voice Assistant. It can perform several functions like text-to-speech, speech-to-text, note taking, web navigation, calculation, Wikipedia search, querying OpenAI and more.


![coin](https://github.com/EdisonWhale/Personal_Pratice_Small_Projects/assets/103423072/85361e78-562b-4bd0-96a3-322b17192cd5)

## Dependencies

The program uses the following Python libraries:

- contextlib
- ctypes
- time
- pygame
- google.cloud.texttospeech
- datetime
- speech_recognition
- pyttsx3
- webbrowser
- wikipedia
- wolframalpha
- keyboard
- openai
- os
- dotenv

Ensure you have all these dependencies installed. If not, you can install via pip:

```bash
pip install pygame google-cloud-texttospeech datetime speechrecognition pyttsx3 wikipedia wolframalpha keyboard openai python-dotenv
```

## Getting Started
To use the voice assistant, follow these steps:

Set up Google Text-to-Speech and OpenAI credentials: Add your Google TTS and OpenAI keys in a .env file at the root of the project.
Run the script with `python3 script_name.py.`

## Usage

The Voice Assistant can be activated with several keywords: 'computer', 'calcutron', 'shodan', 'showdown'.

Here are a few commands that can be used with the voice assistant:

- **Say:** Have the voice assistant speak a message.
  - Example: 'computer say hello'
- **Query OpenAI:** Query the OpenAI API. Use 'Friday' as the command keyword.
  - Example: 'computer Friday what is the weather like?'
- **Go to:** Navigate to a specific website.
  - Example: 'computer go to www.github.com'
- **Wikipedia:** Query Wikipedia for information.
  - Example: 'computer wikipedia Python programming language'
- **Calculate:** Perform calculations. You can use 'calculate' or 'compute' as the command keyword.
  - Example: 'computer calculate 2 plus 2'
- **Log:** Record a note. The note will be saved with a timestamp in the filename.
  - Example: 'computer log Meeting with John at 10am tomorrow'
- **Exit:** Exit the voice assistant.
  - Example: 'computer exit'

## Troubleshooting
If you encounter any issues with the voice assistant, please ensure all dependencies are correctly installed and that your Google TTS and OpenAI API keys are correctly set in your .env file.


## Contact

For more information, questions, or suggestions, please feel free to reach out at:

Edison@gatech.edu

---

Made with ❤️ by Edison  
[www.Edisonwhale.com](http://www.edisonwhale.com)

Have any questions?  
Email me!  
Edison@gatech.edu
