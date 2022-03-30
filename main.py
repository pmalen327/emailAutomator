import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
message = "Put message here"
msg.attach(MIMEText(message))

sender_email = "SENDINGFROM@example.com" #email you're sending FROM
receiver_email = "SENDINGTO@example.com" #email you're sending TO
password = "PASSWORD" #your password to which is used to login remotely

mailserver = smtplib.SMTP('smtp.gmail.com',587) #uses Gmail, a different server can be used, port number is usually 587

# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login(sender_email, password)

mailserver.sendmail(sender_email,receiver_email,msg.as_string())

mailserver.quit()
