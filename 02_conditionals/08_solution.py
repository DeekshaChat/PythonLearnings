password = input("Enter your password: ")

if len(password) < 6:
    print("Weak Password")
elif len(password) < 11:
    print("Medium Password")
else:
    print("Strong Password")
