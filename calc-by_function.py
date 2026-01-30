def calculator(a,b,op):
    if op=='+':
     return a+b
    elif op=='-':
     return a-b
    elif op=='*':
     return a* b
    elif op=='/':
     return a/b
    else:
      return "invalid operator is used "
cal=int(input("enter 1 to enter the calculator and 0 to exit"))
while cal==1:
 num1=int(input("enter the first   number  :"))
 num2=int(input("enter the second number :"))
 op=input("enter a operaotor(-,+,*,/)    :")
 
 print(num1,op,num2 ,'=',calculator(num1,num2,op))
 exit=int(input("enter any number to do  more calculations or 0 to exit the calculator"))

 if exit==0:
   break
 else:
   continue
 
 


