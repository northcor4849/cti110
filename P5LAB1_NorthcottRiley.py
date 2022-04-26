def laps_to_miles(user_laps):
    miles = user_laps / 4
    return miles
# Define your function here 

if __name__ == '__main__':
    user_laps = float(input())
    print(f'{laps_to_miles(user_laps):.2f}')