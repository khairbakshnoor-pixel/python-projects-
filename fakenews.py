import random
actors=['sharukh khan','Virat kholi','Amir Khan','Rohit Sharma']
actions=['launches ','cancels','dances with','eats']
objects=['at Mumbai fort',"at taj mahal",'Anushka ',' a plate samosa']
print("Welcome to Fake Headlines app")
while True:
    subjects=random.choice(actors)
    new=random.choice(actions)
    place=random.choice(objects)
   
    choice=input("Enter your choice (y/n)")
    if choice=='y':
        
     print(f"Breaking {subjects} {new} {place}")

    elif choice=="n":
        print("thanks")
        break
    else:
       print("invalid choice")