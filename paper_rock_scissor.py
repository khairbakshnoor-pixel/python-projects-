# #logic 
# paper
# paper=paper Tie 
# paper rock paper won
# paper scissor scisor won

# rock
# rock paper paper won
# rock scissor  rock won
# rock rock Tie 

# scissor
# scissr=scisor  Time
# scissor rock rock won
# scissor paper scissr won
print("welcome to paper rock scissor game ")

while(True):
  
    import random as rand
    items=["rock","scissor","paper"]

    user=input("Enter your choice (SCISSOR : ROCK PAPER)   0 to exit : ").lower()
    computer=rand.choice(items)

    print(f"user choice = {user}  computer choice  = {computer}")

    if user==computer:
        print("BOTH CHOOSE SAME : MATCH Tied")
    elif user=="rock":
        if computer == "paper":
            print("paper covers rock   computer win")
        else:
            print(" rock thrash scissor user wins")
    elif user =="paper":
        if computer=="rock":
            print("paper cover rock user won")
        else:
            print("scissor cut the paper  computer won")
    elif user =="scissor":
        if computer=="paper":
            print("scissor cut the paper  user won")
        else:
            print("rock thrash scissor computer won")
    if user=="0":
        break
