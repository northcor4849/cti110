# This program will calculate subtotal, sales tax and overall total.
# 2/22/2022
# CTI-110 P2HW1 - Total Purchases
# Riley Northcott


# variables
# Declare variables
# subtotal, sales tax and overall total

subtotal = 0.0
salestax = 0.0
item1 = 0.0
item2 = 0.0
item3 = 0.0
item4 = 0.0
item5 = 0.0

# constants

SALESTAX_RATE = .07


# Input
# Get overall total

item1 = float(input("Enter the price of item #1: "))
item2 = float(input("Enter the price of item #2: "))
item3 = float(input("Enter the price of item #3: "))
item4 = float(input("Enter the price of item #4: "))
item5 = float(input("Enter the price of item #5: "))

# calculations
# Calculate subtotal, sales tax and overall total

subtotal = item1 + item2 + item3 + item4 + item5
salestax = subtotal * SALESTAX_RATE
overalltotal = subtotal + salestax

# display the output


print ("Subtotal: $",format( subtotal,'.2f'),".",sep='')
print ("Sales Tax: $", format( salestax,'.2f'),sep='')
print ("Total: $", format(overalltotal,',.2f'),sep='')













