print"Let's get Started !"
spyname = raw_input("What is your name ? ")
salutation = raw_input("You are Male or female ?" )
if salutation.lower() == "male":
    print 'Welcome MR.' + spyname +' Glad to have you back'
elif salutation.upper() == "FEMALE":
    print 'Welcome Miss. ' +spyname +' Glad to have you back'
else:
    print'Sorry ! Select a Salutation First'
