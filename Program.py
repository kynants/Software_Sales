# Prompt Message
quan = int(input("How many packages are you purchasing? "))

# Discount Amount
if 10 <= quan <= 19:
    disc = 0.2
elif 20 <= quan <= 49:
    disc = 0.3
elif 50 <= quan <= 99:
    disc = 0.4
elif quan >= 100:
    disc = 0.5
else:
    print('Invalid option')

# Discount & Price Calculation
discAmt = (99 * quan) * disc
totalPrice = (quan * 99) - ((99 * quan) * disc)

# Output Result
print('Amount of discount: ${0:.2f}'.format(round(discAmt, 2)))
print('Total amount of purchase: ${0:.2f}'.format(round(totalPrice, 2)))