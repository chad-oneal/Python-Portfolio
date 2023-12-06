import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "chadoneal3@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "chadoneal3@gmail.com"
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Send the email
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
