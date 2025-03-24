
name = input("Enter your name")
age = int(input("Enter your age"))
while age < 0 or age > 18:
    print("Please enter an age that is greater than - and smaller than 18")
    age = int(input("Enter a valid age"))
print("please enter the talent show")