#!/usr/bin/python3
import smtplib
import datetime
import os

# Create these environment variables in .profile,or another appropriate location
# See `change.profile.txt` in the repo for more details
#export PYMAIL_USER_NAME=""
#export PYMAIL_USER_PSWD=""
#export PYMAIL_FWD_ADDR=""
#export PYMAIL_FRM_ADDR=""

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pytz import reference

# collect values from environment variables
fromaddr = os.environ.get('PYMAIL_FRM_ADDR')
toaddr = os.environ.get('PYMAIL_FWD_ADDR')
userid = os.environ.get('PYMAIL_USER_NAME')
paswrd = os.environ.get('PYMAIL_USER_PSWD')
# Get the local time
localtime = reference.LocalTimezone()
rightnow = datetime.datetime.now()
currtz = localtime.tzname(rightnow)
currtime = str(rightnow)
# get the hostname from /etc/hostname
handle = open("/etc/hostname", "r")
myhostname = handle.readline().rstrip('\n')
handle.close()
# Build the message
thesubject = "Raspberry Pi reboot report"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = thesubject
body = "\n" + myhostname + " has experienced a reboot.\n\nThe current time is: " + currtime + " " + currtz
msg.attach(MIMEText(body, 'plain'))
# declare SMTP server & open  secure TLS connection
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
# login to SMTP server using credentials 
server.login(userid, paswrd)
# deliver the mail
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
