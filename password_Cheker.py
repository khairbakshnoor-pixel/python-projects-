password=input("enter a strong password ")
import string
special=False
upp=False
low=True
if len(password)<8  or  len(password)>12:
        print("your password must be atleast 8 chacter and atmost 12")
else:
        for i in password:
         if  i in string.punctuation:
            special=True
         if i in string.ascii_uppercase:
            upp=True
            if upp==True:
                print("your pass must have a uppercase leter")
         if i in string.ascii_lowercase:
             special=True
        if special and low and upp==True:
         print("pass is accepted") 
        else:
         print("your pass must be a speial character uppper or lower case letter")
        

        
        