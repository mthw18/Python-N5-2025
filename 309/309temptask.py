for index in range (0,5):
    temperature = input("Enter a number between -20 and +50")
    if temperature < -20 or temperature > 50:
        print("Enter a valid temperature")
    if temperature > -20 or temperature < 50:
        print("Accepted temperature")
