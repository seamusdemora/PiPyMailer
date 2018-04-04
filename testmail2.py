#!/usr/bin/python3
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pytz import reference

fromaddr = "myusername@gmail.com"
toaddr = "anotherusername@anotherdomain.com"
thesubject = "Raspberry Pi reboot report"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = thesubject

# localtimezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
localtime = reference.LocalTimezone()
rightnow = datetime.datetime.now()
currtz = localtime.tzname(rightnow)
currtime = str(rightnow)
body = "\nYour Raspberry Pi has experienced a reboot.\n\nThe current time is: " + currtime + " " + currtz
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "GMailPassword")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
