# zhacksymcamewxwl
from email.message import EmailMessage
import ssl
import smtplib
import password

email_sender = 'hayatscodes@gmail.com'
emai_password = password.email_password
# Generated from https://temp-mail.org/en/
email_receiver = 'bahoji3076@cnxcoin.com'
subject = "Don't forget to subscribe"

body = """
When you watch a video, please hit subscribe
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

mail_context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=mail_context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())