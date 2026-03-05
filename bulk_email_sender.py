import smtplib

sender = "your_email@gmail.com"
password = "your_password"

receiver = input("Enter receiver email: ")
message = "Hello! This is a test email from Python."

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)

server.sendmail(sender, receiver, message)

print("Email sent successfully")

server.quit()
