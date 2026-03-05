import re

password = input("Enter password: ")

length = len(password) >= 8
uppercase = re.search("[A-Z]", password)
lowercase = re.search("[a-z]", password)
digit = re.search("[0-9]", password)
special = re.search("[@#$%^&+=]", password)

if length and uppercase and lowercase and digit and special:
    print("Strong Password")
else:
    print("Weak Password")
