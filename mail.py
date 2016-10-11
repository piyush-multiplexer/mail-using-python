import smtplib
import getpass

to = raw_input("Enter Receipient: " )
servername = raw_input("Enter Mail Server: ")
username = raw_input("Enter Your Email: ")
password = getpass.getpass("%s's password: " % username)
subject = """Subject: SMTP Test Mail
This is a Test mail message.. 
"""

server = smtplib.SMTP(servername,587)
try:
	server.set_debuglevel(True)	
	server.ehlo()
	if server.has_extn('STARTTLS'):
		server.starttls()
		server.ehlo()

	server.login(username, password)
	server.sendmail(username, to, subject)
finally:
	server.quit()
