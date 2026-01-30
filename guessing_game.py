def check(chance):
  chance -= 1
  if chance>0:
    print('Tries left:',chance)
  else:
    print('Game over!!! No more chances')
  return chance

import random
print('Welcome to the guessing game!!!')
print('Choose a difficulty level:')
print('1. Easy (Number: 1-10, Tries:5)')
print('2. Medium (Number: 1-50, Tries:4)')
print('3. Hard (Number: 1-100, Tries:3)')
choice = input('Enter 1, 2 or 3: ')
chance=5
if choice == '1':
  max_num = 10
  tries = 5
  if chance ==4:
    print("10 points")
  elif chance ==3:
    print("8 points")
  elif chance ==2:
    print("6 points")
  elif chance ==1:
    print("4 points")
  elif chance ==0:
    print("2 points")
  else:
    print("00 points")

elif choice == '2':
  max_num = 50
  tries = 4

elif choice == '3':
  max_num = 100
  tries = 3
else:
  print('Invalid choice - starting game in easy mode')
  max_num = 10
  tries = 5

secret_number = random.randint(1,max_num) #randint is used for random integers
chance = tries
while chance>0:
  guess = int(input('Enter your guess: '))
  if guess == secret_number:
    print('You guessed it right!!!')
    break
  elif guess>secret_number:
    print('Your guess is too high. Try again')
    chance = check(chance)
  elif guess<secret_number:
    print('Your guess is too low. Try again')
    chance = check(chance)
print('The correct answer was',secret_number)
