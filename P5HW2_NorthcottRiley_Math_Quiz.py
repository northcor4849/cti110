# A simple math quiz code
# 4/14/2022
# CTI-110 P5HW2 - Math Quiz
# Riley Northcott
#

def main():
    menu()
    
def menu():
    repeat = 1
    choice = 0
    #scorelist = []
    print("Welcome to Math Quiz")
    while repeat != 0:
        print()
        print( )
        print("MAIN MENU")
        print('---------------')
        print('1. Adding Random Numbers')
        print('2. Subtracting Random Numbers')
        print('3. Exit')
        print('------------')


        choice = input("Please choose one of the menu options: ")
        if choice == '1':
            print("Add Number")
            addnumbers()
        elif choice == '2':
            print("Subtract Numbers")
            subtractnumbers()
    
        elif choice == '3':
            repeat = 0
        else:
            print("Not a valid entry")
            print("Try again")
            repeat = 1
            
    print('Thank you for playing...')
    print('Bye!!')

def addnumbers():
    count = 1
    import random
    num1 = (random.randint(1,10))
    num2 = (random.randint(1,10))
    print(num1)
    print("+", num2)
    answer = num1+num2
    user_input = int(input("Enter Answer.\n"))
    while user_input != answer:
        if user_input < answer:
            print("Sorry, guess is too low. \n")
            count +=1
        else:
            print ("Sorry, guess is too high. \n")
            count +=1
        user_input = int(input('Try Again: '))
    print("Congratulations!!!! your answer is correct..")
    print("Number of guesses:", count)
    
def subtractnumbers():
    count = 1
    import random
    num1 = (random.randint(1,10))
    num2 = (random.randint(1,10))
    print(num1)
    print("-", num2)
    answer = num1-num2
    user_input = int(input("Enter Answer.\n"))
    while user_input != answer:
        if user_input < answer:
            print("Sorry, guess is too low. \n")
            count +=1
        else:
            print ("Sorry, guess is too high. \n")
            count +=1
        user_input = int(input('Try Again: '))
    print("Congratulations!!!! your answer is correct..")
    print("Number of guesses:", count)
 
             


main()



