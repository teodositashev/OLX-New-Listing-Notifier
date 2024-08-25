import ssl
import smtplib
from email.message import EmailMessage

PORT_VALUE = 465

def create_email(sender_email, receiver_email, subject, ads):
    """Prepares an Email contents that will be sent."""

    body = "<html><body>"
    
    for ad in ads:
        #img_html = f'<img src="{ad["image_src"]}" style="width: 100px;" />' if ad['image_src'] else ""
        body += f"""
        <div style="margin-bottom: 20px;">
            <h4>{ad[0]}</h4>
            <p>Цена: {ad[1]}</p>
            <p><a href="{ad[2]}">Линк към обявата</a></p>
        </div>
        <hr>
        """

    body += "</body></html>"
    
    email = EmailMessage()
    email['From'] = sender_email
    email['To'] = receiver_email
    email['Subject'] = subject
    email.set_content(body, subtype='html')
    
    return email

def send_email(email, sender_email, password):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', PORT_VALUE, context=context) as smtp:
        smtp.login(sender_email, password)
        smtp.sendmail(sender_email, email['To'], email.as_string())
