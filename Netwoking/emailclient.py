import smtplib
from email.mime.text import MIMEText

body = "This is a test email.How are you ??"

msg = MIMEText(body)
msg['From'] = "shubhashree09nanda2@gmail.com"
msg['To'] = "mitun09nanda2@gmail.com"
msg['Subject'] = "Hello"

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login("shubhashree09nanda2@gmail.com","lbxg bluc rnwh pulj")

server.send_message(msg)

print("Mail sent")

server.quit()