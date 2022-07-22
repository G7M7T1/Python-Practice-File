import re

regex_1 = r"[A-Za-z0-9._+-]+@[A-Za-z0-9._+-]+\.[A-Za-z]{2,}"
regex_2 = r"[^@]+@[^@]+\.[^@]+"


def check_email_1(email):
    if re.fullmatch(regex_1, email):
        print(f"{email} is a valid email")
    else:
        print(f"{email} not good!!!!!!!")


def check_email_2(email):
    if re.fullmatch(regex_2, email):
        print(f"{email} is a valid email")
    else:
        print(f"{email} not good!!!!!!!")


email_1 = "safafasdas@safasdas.com"
email_2 = "5415asdfas@sa54.com"
email_3 = "5415asdfas@sa54.co3"
email_4 = "5415a-sdfas@sa54.cosd"
email_5 = "5415a_sdfas@sa54.cosd"

check_email_1(email_1)
check_email_1(email_2)
check_email_1(email_3)
check_email_1(email_4)
check_email_1(email_5)

print("-------------------")

check_email_2(email_1)
check_email_2(email_2)
check_email_2(email_3)
check_email_2(email_4)
check_email_2(email_5)