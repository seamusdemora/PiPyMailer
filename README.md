# PiPyMailer

### Notice of Deprecation:

I've not used this in a while for several reasons. I have left it here b/c I thought it may be useful or instructive to others. However, I recently learned that Google no longer allows their mail servers to be used as forwarders - under any circumstances as I understand it. And so, I am marking this as deprecated for now; it will be removed "soon" - in the Newtonian sense of [space-time](https://en.wikipedia.org/wiki/Spacetime). 

Function: Sends email notification when Raspberry Pi experiences a reboot. The Python program is called from a "@reboot" entry in the `crontab` file.

Language: Written in Python

Other Resources: 

* A Gmail account to act as an SMTP forwarder; i.e. Gmail forwards the email created in the script to another email account that the user monitors. ALSO: You'll need to [change a default option in Gmail to allow less secure apps.](https://myaccount.google.com/lesssecureapps) 
* An entry in the local bash profile `~/.profile` (see change.profile.txt) 
* An entry in `crontab` that causes execution of the program during re-boot (see change.crontab.txt).



Ideas and code from [Nael Shiab's (now deprecated) tutorial](http://naelshiab.com/tutorial-send-email-python/) were used in this project.
