''' STARTING OUT WITH PROGRAMMING LOGIC & DESIGN: CHAPTER 4 - MODULES
A software company sells a package that retails for $99. Quantity discounts are
given according to the following table:

Quantity        Discount
10-19           20%
20-49           30%
50-99           40%
100 or more     50%

Design a program that asks the user to enter the number of packages purchased.
The program should then display the amount of the discount (if any) and the
total amount of the purchase after the discount.
'''

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