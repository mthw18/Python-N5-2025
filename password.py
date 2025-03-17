# Program 3 - Investigate and modify
password = input("Please enter your password: ")
while len(password) < 8:
    print("Error, password is mor than 8 characters long.")
    password = input("Please enter your password: ")
print("Password accepted.")
