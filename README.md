# PiPyMailer

Function: Sends email notification when Raspberry Pi experiences a reboot. The Python program is called from a "@reboot" entry in the `crontab` file.

Language: Written in Python

Other Resources: 

* A Gmail account to act as an SMTP forwarder; i.e. Gmail forwards the email created in the script to another email account that the user monitors. ALSO: You'll need to [change a default option in Gmail to allow less secure apps.](https://myaccount.google.com/lesssecureapps) 
* An entry in the local bash profile `~/.profile` (see change.profile.txt) 
* An entry in `crontab` that causes execution of the program during re-boot (see change.crontab.txt).

