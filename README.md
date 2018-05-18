# PiPyMailer

Function: Sends email notification when Raspberry Pi experiences a reboot. The Python program is called from a "@reboot" entry in the `crontab` file.

Language: Written in Python

Other Resources: 

* A Gmail account to act as an SMTP forwarder; i.e. Gmail forwards the email created in the script to another email account that the user monitors. There's a [tutorial that covers this](http://naelshiab.com/tutorial-send-email-python/)
* an entry in the `crontab` file (see change.crontab.txt) 
* an entry in `crontab` that causes execution of the program during re-boot (see change.crontab.txt).

