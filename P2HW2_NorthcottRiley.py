# CTI-110
# P2HW2 - Score Avg
# Riley Northcott 
# 2/24/2022

# create a list
num_list = []
num = float(input("Enter score #1: "))
num_list.append(num)
num = float(input("Enter score #2: "))
num_list.append(num)
num = float(input("Enter score #3: "))
num_list.append(num)
num = float(input("Enter score #4: "))
num_list.append(num)
num = float(input("Enter score #5: "))
num_list.append(num)
num = float(input("Enter score #6: "))
num_list.append(num)
num = float(input("Enter score #7: "))
num_list.append(num)


print(num_list)
#remove the lowest value
lowest = min(num_list)

print('Lowest',lowest)
num_list.remove(lowest)
print(num_list)
total = sum(num_list)
#print(total)
length = len(num_list)
#print(length)
average = total/length

print('-------------Results---------')
print('Lowest Score:',lowest)
print("Modified List: ",num_list)
print("Scores Average: ", format(average,'.2f'))
# sort the list and use pop to remove index 0

##num_list.sort()
##num_list.pop(0)
##print (num_list)
