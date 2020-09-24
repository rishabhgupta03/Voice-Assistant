import smtplib
import pyttsx3
import main


def send(to, sub, body):
    conn = smtplib.SMTP('smtp.gmail.com', 587)

    conn.ehlo()

    conn.starttls()

    conn.login('rg12032001@gmail.com', 'J7d@!Mf%')

    conn.sendmail('rg12032001@gmail.com', to, 'Subject : ' + sub + '\n\n' + body)

    conn.quit()

    pyttsx3.speak('mail sent successfully')