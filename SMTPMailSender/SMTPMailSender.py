import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

msg = MIMEMultipart()
msg["From"] = ""
msg["To"] = ""
msg["Subject"] = ""

text = """ """

msg_body = MIMEText(text, "plain")
msg.attach(msg_body)

# Gmail Server verbinden

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("", "")
    mail.sendmail(msg["From"], msg["To"], msg.as_string())

    print("Mail wurde erfolgreich gesendet.")
    mail.close()
except:
    sys.stderr.write("Fehler aufgetreten.")
    sys.stderr.flush()
