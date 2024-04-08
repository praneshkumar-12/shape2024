import smtplib
from email.message import EmailMessage
import os


def send_email(to, subject, content):
    user = "YOUR_MAIL"
    key = "YOUR_KEY"

    msg = EmailMessage()

    msg["Subject"] = subject

    msg["From"] = user

    msg["To"] = to

    msg.set_content(content)

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(user, key)
    server.send_message(msg)
    server.quit()