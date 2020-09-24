from selenium import webdriver
import time
import pyttsx3

# CUSTOM MODULES
import main


def whatsapp_send(name, msg):
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com')
    time.sleep(5)
    # name = input("whom do you want to send message")
    user = driver.find_element_by_xpath('//span[@title= "{}"]'.format(name))
    time.sleep(3)
    user.click()
    time.sleep(1)
    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
    msg_box.send_keys(msg)
    msg_send = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
    msg_send.click()


def askinfo():
    main.respond("whom do you want to send message?")
    user = main.listen()
    main.respond(f"please tell me the message to send to {user}")
    message = main.listen()
    main.respond("scan QR code in the next screen to continue login to whatsapp")
    whatsapp_send(user, message)
    main.respond("message send as you said, sir!")
