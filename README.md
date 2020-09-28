# Voice-Assistant

This is a simple virtual assistant written in Python 3.

[![Watch the video](https://drive.google.com/file/d/1eDrGoe3ID1LTuLvyO1KbA7xZf6Pkf-oH/view?usp=sharing")](https://drive.google.com/file/d/1eDrGoe3ID1LTuLvyO1KbA7xZf6Pkf-oH/view?usp=sharing")

## Voice-Assistant Architecture
Virtual assistants are built from the following components:
* Voice Activity Detection (VAD) - this determines when the user starts and stops speaking. Voice-Assistant uses the python [SpeechRecognition](https://github.com/Uberi/speech_recognition) module for VAD.
* Speech to Text (STT) - This converts the audio that was recorded between when the VAD recognized that the user started speaking and when the user ended speaking. Voice-Assistant uses the default STT provider for the python SpeechRecognition module, which is currently a free online service from Google called "Google Speech Recognition". The SpeechRecognition module can also use Pocketsphinx for offline recognition.
* Text to Intent - This takes the recognized text from the STT engine and figures out what action you want the assistant to perform. Usually the full recognized text is passed to the action to search for keywords. This is the bulk of what the digital_assistant method in the main.py script does.
* Action - this performs some action based on the intent. It usually responds with a text message.
* Text to Speech (TTS) - this converts text, usually returned by an action, to speech which is then played by the computer as a response.

## Installation

### Windows
Voice-Assistant runs well on Windows. For the easiest setup, you should probably download and install [Anaconda](https://www.anaconda.com/products/individual) and then use the conda command with the environment.yml file from the Anaconda prompt to create a virtual environment for yourself.

```dos
(base) C:\Projects\Voice-Assistant>conda env create -f environment.yml
(base) C:\Projects\Voice-Assistant>conda activate Voice-Assistant
(Voice-Assistant) C:\Projects\Voice-Assistant>python main.py
```

### Linux
Voice-Assistant works well with Linux. It should run on a Raspberry Pi or other SBC or within Linux installed on a virtual machine like on VirtualBox.

Most Linux distros already have Python 3 installed.

You should always use Voice Assistant within a virtual environment, especially on Linux where system utilities are likely to be written in your system Python. Getting your system environment messed up when a required library gets changed is never fun.

On Debian derivates like Ubuntu, Mint, Raspbian, etc. you can install a virtual environment using VirtualEnvWrapper:

```bash
~/Voice-Assistant $ sudo apt install virtualenvwrapper
~/Voice-Assistant $ echo ". /usr/share/virtualenvwrapper/virtualenvwrapper.sh" >> ~/.bashrc
~/Voice-Assistant $ . /usr/share/virtualenvwrapper/virtualenvwrapper.sh
~/Voice-Assistant $ mkvirtualenv -p /usr/bin/python3 Voice-Assistant
(Voice-Assistant) ~/Voice-Assistant $
```

You will probably need to install eSpeak and PortAudio. On Debian derivatives like Ubuntu, Mint, Raspbian, etc. these can be installed with:

```
Voice-Assistant $ sudo apt install portaudio19-dev libespeak-dev
```
then activate your virtual environment and use the requirements.txt file to load the required modules:
```
~/Voice-Assistant $ workon Voice-Assistant
(Voice-Assistant) ~/Voice-Assistant $ pip install -r requirements.txt

To run Voice-Assistant, you should activate the virtual environment, then use python to run the main.py script:

```
~/Voice-Assistant $ workon Voice-Assistant
(Voice-Assistant) ~/Voice-Assistant $ python main.py
```
