# CTI-110
# P3HW2 - Pizza Order
# Riley Northcott
# 3/10/2022
#

numberPeople = int(input("How many students do you want to order pizza for? "))

# Calculations
# get number of pizzas
numberPizzas = numberPeople / 2

# number of slices
numberSlices = numberPeople * 3



people = float(input("Enter number of people per pizza ( 1.5, 2 or 3): "))
if people == 1.5:
    numberPizzas = numberPeople / 1.5
    price = numberPizzas * 5 * 1.06
    print("----Pizza Order-------")
    print("Number of Students : ", numberPeople)
    numberPizzas = int(round(numberPizzas,0))
    print("Pizzas Needed : ", numberPizzas)
    print("Price $", format(price,',.2f'), sep='')
elif people == 2:
    numberPizzas = numberPeople / 2
    price = numberPizzas * 5 * 1.06
    print("----Pizza Order-------")
    print("Number of Students : ", numberPeople)
    numberPizzas = int(round(numberPizzas,0))
    print("Pizzas Needed : ", numberPizzas)
    print("Price $", format(price,',.2f'), sep='')
elif people == 3:
    numberPizzas = numberPeople / 3
    price = numberPizzas * 5 * 1.06
    print("----Pizza Order-------")
    print("Number of Students : ", numberPeople)
    numberPizzas = int(round(numberPizzas,0))
    print("Pizzas Needed : ", numberPizzas)
    print("Price $", format(price,',.2f'), sep='')
else:
    print("INVALID ENTRY!!!")
    print("Should have entered 1.5, 2 or 3")
    print()
    print("Run program again")
















