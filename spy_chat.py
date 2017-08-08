print"Let's get Started !"
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


else:
    print "Dude What's wrong with you ? Please Enter your Name ! "




