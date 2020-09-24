import webbrowser
import bs4
import requests
import pyttsx3
import time


def wikipedia(topic):
    global elem
    res = requests.get('https://en.wikipedia.org/wiki/' + topic)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    time.sleep(2)
    try:
        elem = soup.select('#mw-content-text > div.mw-parser-output')
    except IndexError:
        pyttsx3.speak("sorry couldn't find that! please try again or try searching with different keywords")
    file = open(f'C:\\Users\\Asus\\Desktop\\{topic}.txt', 'w+', errors='ignore')
    content = elem[0].text
    file.write(content)
    file.close()
    pyttsx3.speak(f'file have been saved on your desktop. you may read about {topic} any time through that file.')
    time.sleep(8)
