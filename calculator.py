num=int(input("enter 1 to go to calculator"))
while(num==1):
  a=int(input("enter the number       :"))
  b=int(input("enter the second number        :"))
  c=input("enter the operator(+,-,*,/,%,^)        :")
  
  if c=='+':
   print('sum is  ',a+b)
  elif c=='-':
   sub=a-b
   print('sub is',sub)
  elif c=='/':
     if a<b:
       print("invalid")
     div=a/b
     print('division is',div)
  elif c=='*':
      mul=a*b
      print('multiplication is',mul)
  elif c=='%':
    mod=a%b
    print('modulus is ',mod)
  elif c=='^':
    power=a**b
    print('power is ',power)
  exit=int(input("for exiting press 0 or again calculator press 1   "))
  if exit==1:
    print("RE USE 1for using my calculator")
  else:
     break



