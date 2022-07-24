import smtplib
import getpass

smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)

# Hello ESMTP
smtp_obj.ehlo()

# Encrypted
smtp_obj.starttls()

# Login in Mail
email = input("Enter Your Email: ")
password = getpass.getpass("Enter Your Password: ")
# username password
smtp_obj.login(email, password)

# From and To
from_address = email
to_address = email

subject = input("Enter Subject: ")
message = input("Enter Message: ")

full_message = "Subject: " + subject + "\n" + message

smtp_obj.sendmail(from_address, to_address, full_message)
smtp_obj.quit()
