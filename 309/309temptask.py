temperature = []
for index in range(0,5):
    temp = input("Enter a daily temperature between -20 and +50")
    while temperature < -20 or temperature > 50:
        print("These are invalid temperatures")
        temp = int(input("Please re-enter a valid temperature"))
temperature.append(temp)    