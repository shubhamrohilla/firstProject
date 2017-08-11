print"Let's get Started !"
#enter name of spy.
spyname = raw_input("What is your name ? ")
spyname=" ".join(spyname.split())
if len(spyname)>0:
    if spyname.isdigit():
        print "You can not enter Numeric value in Name,please try again !"

    else:
        salutation = raw_input("You are Male or female ?")


        if salutation.lower() == "male":
            print 'Welcome MR.' + spyname + ' Glad to have you back'
        elif salutation.upper() == "FEMALE":
            print 'Welcome Miss. ' + spyname + ' Glad to have you back'
        else:
            print'Sorry ! Enter a Salutation First'

        print "We Would like to known more about you !"

        spyage = raw_input("Enter Your age.")
        # while (spyage.isalnum()==True):
        #   print "Hey Don't Enter Alpha-numeric characters"
        if spyage.isalpha():
            print 'Please enter your age in Numeric form'
            # elif spyage.isalnum()==True:
            # print"Hey Don't Enter Alpha-numeric characters"
        elif ((int(spyage) > 18) and (int(spyage) < 50)):
            print "Hola !!! You can be a Spy."
        else:
            print "Sorry You Cant be a Spy.You should have a Valid age."

        spyrating = raw_input("Enter the Rating you want to give to spy out of 10.")
        if spyrating.isalpha():
            print "Please Enter in Numeric form."
        elif ((float(spyrating) > 0) and float(spyrating) <= 10):
            print "Spy rating is " + spyrating

            if ((float(spyrating) > 0) and float(spyrating) <= 4):
                print "Poor Performance"
            elif ((float(spyrating) > 4) and float(spyrating) <= 6):
                print "Average Performance "
            elif ((float(spyrating) > 6) and float(spyrating) <= 8):
                print "Good Performance "
            else:
                print "Excellent Performance "

        else:
            print "please enter a valid rating"

else:
    print "Dude What's wrong with you ? Please Enter your Name ! "











