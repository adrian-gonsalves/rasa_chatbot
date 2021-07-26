import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mail_user(message, user_email):
	mail_content = message
	#The mail addresses and password
	sender_address = 'mlai.discuss@gmail.com'
	sender_pass = 'your password'
	receiver_address = user_email
	#Setup the MIME
	message = MIMEMultipart()
	message['From'] = 'Foodie Restaurants Search'
	message['To'] = receiver_address
	message['Subject'] = 'Top 10 Restaurants'   #The subject line
	#The body and the attachments for the mail
	message.attach(MIMEText(mail_content, 'plain'))
	#Create SMTP session for sending the mail
	session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
	session.starttls() #enable security
	session.login(sender_address, sender_pass) #login with mail_id and password
	text = message.as_string()

	session.sendmail(sender_address, receiver_address, text)
	session.quit()
	return 'Mail Sent'
