contacts={}

while True:
    print("WElcome to contact app")
    print("1.create contact")
    print("2.view contact")
    print("3.update contact")
    print("4.delete contact")
    print("5.search contact")
    print("6.length of contact")
    choice=int(input("Enter your choice"))
    if choice==1:
        name=input("Enter the name of the contac")
        if name in contacts:
            print(f"contact name {contacts} already exist")
        else:
            number=input("Enter the  11 digit number")
            contacts[name]={'mobile':number}
            print(f"CONTACT{name}  number {number}created successfully")
    elif choice==2:
        name=input("Enter contact name to view")
        if name in contacts:
            contacts=contacts[name]
            print(f"NAME : {name} MObile number :{number}")
        else:
            print("contact not found")
    elif choice ==3:
        name=input("Enter the name of the contac")
        if name in contacts:
            number=input("Enter the  11 digit number")
            contacts[name]={'mobile':number}
            print(f"CONTACT :{name}  number :{number} updated successfully")
        else:
            print("contact not found")
    elif choice==4:
        name=input("Enter contact name to view")
        if name in contacts:
            del(contacts[name])
            print(f"CONTACT :{name}  deleted  successfully")
        else:
            print("contact not found")
    elif choice==5:
        search=input("Enter the name you want to find")
        found=False
        for name ,contact in contact:
            if search.lower() in name.lower():
                print(f"Found name {name},number {number}")
                found=True
            if not found:
                print("Contact not found")
    elif choice ==6:
        print("the lenght of contact is ",len(contacts))
    elif choice ==7:
        print("exiting")
        break
    else:
        print("invalid choice")


    







