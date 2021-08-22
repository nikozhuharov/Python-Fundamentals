import re
pattern = r"(?<=\s)[A-Za-z0-9]+([-._][A-Za-z0-9]+)*@[A-Za-z]+(-[A-Za-z]+)*(\.[A-Za-z]+(-[A-Za-z]+)*)+"
text = input()
mails = re.finditer(pattern, text)
for mail in mails:
    print(mail.group())
