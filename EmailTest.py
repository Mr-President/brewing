import smtplib

gmail_user = 'ZachsRaspberry@gmail.com'
gmail_password = 'Raspberry1'

sent_from = gmail_user
to = ['6368754769@txt.att.net']
subject = 'Controller Error'
body = 'An error has occured and the temperature controller has failed \nReset the program to maintain control \n-Raspberry Pi'

#email_text = """
#From: %s
#To: %s
#Subject: %s

#%s
#""" % (sent_from,",".join(to),subject,body)
def error():
	try:
		server = smtplib.SMTP_SSL('smtp.gmail.com',465)
		server.ehlo()
		server.login(gmail_user,gmail_password)
		server.sendmail(sent_from,to,body)
		server.close
	except:
		print "Something didnt work"
