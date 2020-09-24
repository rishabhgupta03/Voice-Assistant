import speech_recognition as sr
from selenium import webdriver
import pyttsx3
from time import ctime
import time
import webbrowser as wb
import bs4
import requests

# CUSTOM MODULES
import whatsapp
import weather
import play
import read
import sendmail


def respond(AudioString):
    pyttsx3.speak(AudioString)


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source)
    cmd = ""
    try:
        cmd = r.recognize_google(audio)
        return cmd
    except sr.UnknownValueError:
        respond("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        respond("Request Failed; {0}".format(e))
    return cmd


def digital_assistant(data):
    global sub
    if "how are you" in data:
        pyttsx3.speak("I am well")

    if "what time is it" in data:
        pyttsx3.speak(ctime())

    if "stop listening" in data or "stop" in data or "quit" in data:
        lis = False
        print('Listening stopped')
        return lis

    if ("WhatsApp" or "whatsapp" or "WHATSAPP") in data:
        whatsapp.askinfo()
        # whatsapp.whatsapp_send(user, message)

    if "what can you do" in data:
        respond("can handle pretty much all your stuff, sir! however i am still learning so i'll be able to perform "
                "more task in future")

    if "where is" in data or "navigate to" in data:
        l = data.split(" ")
        loc = " ".join(l[2:])
        location_url = f"https://www.google.com/maps/place/{str(loc)}"
        respond("Hold on Rishabh, I will show you where " + loc + " is.")
        browser = webdriver.Chrome()
        browser.get(location_url)
        time.sleep(1)
        search = browser.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div["
                                               "1]/button")
        search.click()
        time.sleep(3)
    if ("weather" or "climate") in data:
        weather.info(data)

    if "want to watch" in data or "stream" in data:  # i want to watch tanmay bhat on youtube
        l = data.split(" ")
        iofp = l.index("on")
        if "stream" in data:
            video = "+".join(l[2:iofp])
        else:
            video = "+".join(l[4:iofp])
        platform = " ".join(l[iofp + 1:])
        print(platform)
        play.movies(video, platform)

    if "play" in data:
        l = data.split(" ")
        song = " ".join(l[1:])
        play.music(song)

    if "read" in data or "search" in data or "explain" in data or "what is" in data or "details" in data or "what are" in data:
        l = data.split(" ")
        # i = l.index("about")
        topic = l[-1]
        read.wikipedia(topic)

    if "email" in data:
        print(data)
        l = data.split(" ")
        respond("please enter the email address of the recipient")
        to = input()
        if "regarding" in data:
            r = l.index('regarding')
            sub = l[r + 1]
        else:
            respond("please tell me the subject regarding e-mail")
            sub = listen()
        respond("kindly tell me the body of e-mail")
        body = listen()

        sendmail.send(to, sub, body)

    print(data)

    lis: bool = True
    return lis


if __name__ == "__main__":
    pyttsx3.speak("Hello Rishabh. what can i do for you?")
    # time.sleep(1)
    listening = True
    while listening:
        task = listen()
        listening = digital_assistant(task)