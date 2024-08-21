import os
from email.message import EmailMessage
import ssl
import smtplib

PORT_VALUE = 465

#You need to use a gmail account here
email_sender = "sender_email@gmail.com"

#The recieving email doesn't need to be a gmail
email_receiver = "receiver@somemail.com"

email_password = os.environ.get("OLX_NOTIFIER_PASSWORD")

#How often would you like to be notified about new listings
minutes = 30                                                

#add check if it is more than 1 minute to say minutes else to say minute
subject = "Check out the new listings uploaded on OLX in the last " + str(minutes) + " minutes."    
body = """
    There are the following new listings uploaded here:
    1.) Name of first listing
        Picture of first listing
        Link to first listing
    ...
    """

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

email_context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', PORT_VALUE, context = email_context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    