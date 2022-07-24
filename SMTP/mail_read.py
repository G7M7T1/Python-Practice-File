import imaplib
import getpass
import email as em

M = imaplib.IMAP4_SSL("imap.gmail.com")

email = input("Enter Your Email: ")
password = getpass.getpass("Enter Your Password: ")

M.login(email, password)

print("\n")
print("--------- Mail Select List ---------")
print(M.list())
print("--------- Mail Select List ---------")
print("\n")

print("\n")
print("--------- Mail Match ID ---------")
M.select('inbox')
search_result, mail_id = M.search(None, f"FROM {email}")
print(f"Search Result: {search_result}, ID: {mail_id[0]}")
print("--------- Mail Match ID ---------")
print("\n")

print("\n")
print("--------- Mail Fetch ---------")
fetch_result, content = M.fetch(mail_id[0], "(RFC822)")
print(f"Fetch Result: {fetch_result}")
raw_content = content[0][1]
raw_email_content = raw_content.decode("utf-8")
email_message = em.message_from_string(raw_email_content)

for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        with open("email-text.txt", mode="wb") as f:
            f.write(body)
        with open("email-text.txt") as f:
            message = f.read()
            print(message)
print("--------- Mail Fetch ---------")
print("\n")



