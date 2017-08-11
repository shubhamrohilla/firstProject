mylist=[]
mydict={}
keys=int(raw_input("Enter the number."))
for i in range(1,keys+1):

    mydict = mydict.fromkeys(str(i),str(i*i))
    mylist.append(mydict)
print mylist
