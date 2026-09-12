# Exercise 3: Email Domain Extractor


def email_domain_extractor():
    mail = input("Enter the Gmail: ")
    if "@" in mail:
        ind = mail.index("@")
        result = mail[ind+1:]
        print(f"Result is: {result}")
    else:
        print(f"Invalid Email")


email_domain_extractor()
