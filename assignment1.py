number=[] #list for storing the result
for i in range(2000,3201):
    if (i%7==0)and (i%5 !=0):
        number.append(str(i)) #appending result in the corresponding list of number divisible by 7
print(','.join(number))


