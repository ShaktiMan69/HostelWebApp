#! /usr/local/bin/python
SMTPserver = 'smtp.hostinger.com'
sender =     'hostelcompanionapp@ezalts.shop'

USERNAME = "hostelcompanionapp@ezalts.shop"
PASSWORD = "***REMOVED***"

import sys

from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)

# old version
# from email.MIMEText import MIMEText
from email.mime.text import MIMEText

def send_email(destination, content='Congrats', subject='Your application for a Hostel Room has been submitted.'):
    try:
        msg = MIMEText(content, 'plain')
        msg['Subject'] = subject
        msg['From'] = sender # some SMTP servers will do this automatically, not all

        conn = SMTP(SMTPserver)
        conn.set_debuglevel(False)
        conn.login(USERNAME, PASSWORD)
        try:
            conn.sendmail(sender, destination, msg.as_string())
        finally:
            conn.quit()

    except:
        sys.exit( "mail failed; %s" % "CUSTOM_ERROR" ) # give an error message