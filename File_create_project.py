import  os 
def crreatfile(filename):
    try:
        with open(filename,"x") as f:
            print(f"File create {filename}")
    except FileExistsError:
        print(f"file already exit {filename}")
    except Exception as  e:
        print("An Error ocured")
def view_files():
    file=os.listdir()
    if not  file:
        print("file not found")
    else:
        print("file in directory")
        for i in file:
            print(i)
def delete(filename):
    os.remove(filename)
    try:
        print(f"{filename} removed")
    except FileNotFoundError:
        print("file not found")
def read(filename):
    try:
        with open("sales_record.txt",'r') as g:
            content=g.read()
            print(f"content of file name{filename} is {content} ")
    except FileNotFoundError:
        print("file not found")
def edit(filename):
    try:
        with open("sales_record.txt","a") as r:
            content=input("Enter what youwant to enter")
            r.write(content+"\n")
            print(f"file added {filename} sucessfully {content}")
    except FileNotFoundError:
        print("file not found")
    except Exception as  e:
        print("An Error ocured")

def main():
    while True:
        print("WELCOME TO FILE MANAGEMENT SYSTEM")
        print("1.CREATE FILE")
        print("2.VIEW ALL FILE ")
        print("3.DELETE ALL FILE")
        print("4.READ FILE")
        print("5.EDIT FILE")
        print("6.EXIT")
        choice=input("enter your choice")
        if choice=="1":
            filename=input("Enter the file name")
            crreatfile(filename)
        elif choice=='2':
            view_files()
        elif choice=="3":
            filename=input("Enter the name of the file you want to delete")
            delete(filename)
        elif choice=='4':
            filename=input("Enter the file name you want to read")
            read(filename)
        elif choice=="5":
            filename=input("Enter the file name you want to edit")
            edit(filename)
        elif choice=='6':
            print("exiting")
            break
        else:
            print("invalid choice")
if __name__=="__main__":
    main()
        
