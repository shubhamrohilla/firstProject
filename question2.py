count=1
factorialinput=int(raw_input("Enter any number for which you want factorial."))
if factorialinput<0:
    print "Negative Values don't have factorial !"
elif factorialinput==0:
    print "1"
else:
    for i in range(1, factorialinput+1):
        count=count*i
    print count
