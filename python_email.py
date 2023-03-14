import smtplib

sender = None #your email address
receiver = None #send to user
password = None #your App Password from gmail account
subject = "Python Test Email"
body = "Test Email for Python"

#header
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged In...")

    server.sendmail(sender,receiver,message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in, check App Password in Gmail")