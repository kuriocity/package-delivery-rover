import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


email = 'test1@gmail.com'
password = ''
send_to_email = 'test2@gmail.com'
message = 'This is your OTP: 123'
subject = 'This is your OTP: 123'


msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()
