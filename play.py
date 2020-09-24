import main
import webbrowser as wb
import time
import pyautogui


def movies(video, platform):
    if ("Amazon" or "Prime") in platform:
        wb.open("https://www.primevideo.com/search/ref=atv_nb_sr?phrase=" + video)
        time.sleep(2)
        pyautogui.click(274, 423)
    elif "youtube" in platform.lower():
        wb.open('https://www.youtube.com/results?search_query=' + video)
    time.sleep(5)


def music(song):
    wb.open('https://music.youtube.com/search?q=' + song)
    time.sleep(2.5)
    pyautogui.click(560, 324)
    time.sleep(10)
