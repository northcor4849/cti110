# P3HW1- Debugging assignment
# Northcott

def main():
    # This program turns a number grade into a letter grade.

    # This system uses a 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 59


    score = int(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    elif score >= B_score:
        print('Your grade is: B')
    elif score >= C_score:
        print('Your score is :C')
    elif score >= D_score:
        print('Your score is :D')
                
    else:
        print('Your grade is: F')



main()
