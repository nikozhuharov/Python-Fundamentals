def password_validator (password):
    valid = True
    if not 6 <= len(password) <= 10:
        valid = False
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        valid = False
        print("Password must consist only of letters and digits")
    count = 0
    for i in password:
        if i.isnumeric():
            count += 1
    if count < 2:
        valid = False
        print("Password must have at least 2 digits")
    if valid:
        print("Password is valid")


password = input()
password_validator(password)