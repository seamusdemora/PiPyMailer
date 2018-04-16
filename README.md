# PiPyMailer

Function: Notify me by email if my Raspberry Pi experiences a reboot. This function is executed by a "@reboot" entry in the `crontab` file.

Language: Written in Python

Other Resources: 

* A Gmail account to act as an SMTP forwarder; i.e. Gmail forwards the email created in the script to an email account that I monitor. There's a [tutorial that covers this](http://naelshiab.com/tutorial-send-email-python/)
* The [Pendulum module](https://pendulum.eustace.io/docs/#installation) for date-time manipulation 
* an entry in crontab that causes execution of the program during re-boot.

