current_price = int(input())
last_months_price = int(input())

#Read in the input using input()
print ('This house is $',current_price,'.',' The change is $',current_price-last_months_price,' since last month.', sep='')
print ('The estimated monthly mortgage is $',f'{(current_price*0.051)/12:.2f}','.', sep='')
# use the .count()