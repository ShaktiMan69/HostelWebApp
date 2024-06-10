#! /usr/local/bin/python

import os
from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)

# old version
# from email.MIMEText import MIMEText
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

SMTPserver = os.environ.get('SMTPserver')
sender =  os.environ.get('sender')

USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')

print(SMTPserver, sender, USER, PASSWORD)
def send_email(destination, content='Congrats', subject='Your application for a Hostel Room has been submitted.'):
    try:
        msg = MIMEText(content, 'plain')
        msg['Subject'] = subject
        msg['From'] = sender # some SMTP servers will do this automatically, not all

        conn = SMTP(SMTPserver)
        conn.set_debuglevel(False)
        conn.login(USER, PASSWORD)
        try:
            conn.sendmail(sender, destination, msg.as_string())
        finally:
            conn.quit()

    except Exception as e:
        print("mail failed: ", e ) # give an error message

if __name__ == '__main__':
    send_email('***REMOVED***')