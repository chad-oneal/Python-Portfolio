import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "chadoneal3@gmail.com"
    password = "your_password_here"  # replace with your password
    receiver = "chadoneal3@gmail.com"
    # Create a secure SSL context
    context = ssl.create_default_context()
    # Email headers and message
    message = ("""\
From: {sender}
To: {receiver}
Subject: Test Email

Hi!
How are you?
Bye!
""".format(sender=username, receiver=receiver))
    # Send the email
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


send_email()
