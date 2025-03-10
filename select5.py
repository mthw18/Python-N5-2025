price_per_badge = 0.25
noOfBadges = int(input("How many badges do you want to order?"))
total_price = noOfBadges * price_per_badge
if noOfBadges > 150:
    total_price *= 0.9
print("The price of that will be", total_price)