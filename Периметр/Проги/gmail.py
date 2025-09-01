import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

server_address = "smtp.gmail.com"
server_port = 587
login, password = "nikas201107@gmail.com", "kkjg mcyt cblr soym"

msg = MIMEMultipart()
msg['From'], msg['To'], msg['Subject'] = "nikas201107@gmail.com", "hcx08807jgre64@print.epsonconnect.com", "Принтер"
msg.attach(MIMEText("Содержимое письма", 'plain'))

file_path = r"C:\Users\Asus\Downloads\progon.png"
with open(file_path, "rb") as file:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename={file_path}")

msg.attach(part)
with smtplib.SMTP(server_address, server_port) as server:
    server.starttls()
    server.login(login, password)
    server.send_message(msg)
