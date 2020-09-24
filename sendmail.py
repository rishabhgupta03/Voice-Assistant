import smtplib
import pyttsx3
import main


def send(to, sub, body):
    conn = smtplib.SMTP('smtp.gmail.com', 587)

    conn.ehlo()

    conn.starttls()

    conn.login('YOUR_EMAIL_ADDRESS', 'PASSWORD')
    
    

    conn.sendmail('YOUR_EMAIL_ADDRESS', to, 'Subject : ' + sub + '\n\n' + body)

    conn.quit()

    pyttsx3.speak('mail sent successfully')
