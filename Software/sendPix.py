import smtplib

GMAIL_USER = 'billybob@gmail.com'   #replace with valid e-mail address
GMAIL_PASS = '123456789'            #replace with the user's password

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def send_email(recipient, subject, text):
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = "To:" + recipient + "\n" + "From: " + GMAIL_USER
    header = header + "\n" + "subject:" + subject + "\n"
    msg = header + "\n" + text + "\n\n"
    smtpserver.sendmail(GMAIL_USER, recipient, msg)
    smtpserver.close()

def sendPicture():
    send_email(GMAIL_USER, "Dog Picture", "The picture is attached")
