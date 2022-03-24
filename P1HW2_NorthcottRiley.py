# This program will calculate the number of pizzas and slices needed
# Date
# CTI-110 P1HW2 - Pizza Order
# Riley Northcott
#

# variables to hold number of people

numberPeople = int(input("How many students do you want to order pizza for? "))

# Calculations
# get number of pizzas
numberPizzas = numberPeople / 2
# number of slices

numberSlices = numberPeople * 3

# display information

print("----Pizza Order--------")

print ("Number of Students: ", numberPeople)

print ("Pizza Slices Needed:", numberSlices)
      
print ("Pizzas needed:", numberPizzas)
                         
