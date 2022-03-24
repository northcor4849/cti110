# Type your code here
service_list = input('Enter desired auto service:\n')
print('You entered:',service_list)
if service_list == 'Oil change':
    print('Cost of oil change: $35')
elif service_list == 'Tire rotation':
    print('Cost of tire rotation: $19')
elif service_list == 'Car wash':
    print ('Cost of car wash: $7')
else:
    print('Error: Requested service is not recognized')