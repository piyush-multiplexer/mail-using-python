# mail-using-python
smtp mail in python 
 In this 'Sender' and 'Recipient' mail id entered run time.
 'mailserver'(e.g. "smtp.gmail.com") is of google given at run time.
'password' of Sender is given at runtime.

server = smtplib.SMTP(servername,587)
TLS port for gmail(587), if you change mail server then port need to change according to requiremnts.

server.set_debuglevel(True)	, to see the all log info at run time.

