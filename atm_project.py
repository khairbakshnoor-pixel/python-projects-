# 1. ATM management system 


balance=10000
def deposite(amount,balance):
        balance=balance+amount
        return balance

def withdraw(amount,balance):
        if amount<balance:
             balance=balance-amount
             return balance
        else:
            print("insufficient balance")
            return balance
       
def show_balance(balance):
    return balance
       
while(True):
    print("welcome to ATM ")
    print("MENU")
    print("1.deposite MONEY ")
    print("2.withdraw MONEY")
    print("3.show balance")
    print("4. exit")
    
    choice=int(input("Enter your choice     :"))
    if choice==1:
     amount=int(input("Enter the amount you want to deposite"))
     balance=deposite(balance,amount)
    
    elif choice ==2:
       amount=int(input("enter amount you want to withdraw"))
       balance=withdraw(balance,amount)
     
    elif choice==3:
       balance=show_balance(balance)
       print(balance)
    elif choice==4:
       break
    else:
       print("invalid choice")