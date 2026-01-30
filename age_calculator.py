a=int(input("enter your birth year without dashes or underscore"))
age=2025-a
print("your age is",age)
if age>=13 and age<18:
    print("you are a teenager")
elif age>=18:
    print("you are a adult ")
elif age>13:
    print("you are a child")