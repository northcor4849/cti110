# grade calculator
# 4/12/2022
# CTI-110 P5HW1 - Score List
# Riley Northcott
#

def main():
    menu()
    
def menu():
    repeat = 1
    choice = 0
    scorelist = []
    while repeat != 0:
        print()
        print('----MENU----')
        print('1. Create Score List')
        print('2. Display Results')
        print('3. Exit')
        print('------------')


        choice = input("Enter a choice 1 or 2 or 3: ")
        if choice == '1':
           scorelist = listofscores()
        elif choice == '2':
            if len(scorelist) == 0:
                print('List not created!')
            else:
                calcscores(scorelist)
        elif choice == '3':
            repeat = 0
        else:
            print("Not a valid entry")
            print("Try again")
            repeat = 1
            
    print('Program Terminated!')

def makelist(numscores):
    scores = []
    i = 0
    #Gets scores
    while i < numscores:
        score = int(input(f'Enter score #{i + 1}: '))
        #Determines if score is less than zero or greater than 100
        if 0 > score or score > 100:
            print('Invalid Entry!\nEntry must be between 0 and 100!')
            i = i
        else:
            scores.append(score)    #Adds each score to end of list
            i += 1
    return scores
######
def calcscores(scorelist):
 

    #finds lowest score and removes it
    min_score = min(scorelist)
    scorelist.remove(min_score)

    #averages scores list
    average = sum(scorelist)/len(scorelist)

    #Determines letter grade
    if 100 >= average >= 90:
        lettergrade = 'A'
    elif 89 >= average >= 80:
        lettergrade = 'B'
    elif 79 >= average >= 70:
        lettergrade = 'C'
    elif 69 >= average >= 60:
        lettergrade = 'D'
    elif 59 >= average >= 0:
        lettergrade = 'F'

    #puts values into list
    temp = [min_score,scorelist,average,lettergrade]

    #returns list of values
    printscores(temp)

######

def listofscores():
    index = int(input('Enter number of scores: '))
    scorelist = makelist(index)
    return scorelist

######
    
def printscores(resultlist):
    
    
    #prints values
    print('Lowest score:',resultlist[0])
    print('List of scores (lowest omitted):',resultlist[1])
    print('Average:',resultlist[2])
    print('Letter Grade:',resultlist[3])
   


main()
