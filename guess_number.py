from random import randint
number = randint(1, 100)
print('Guess the number from 1 to 100')
while True:
    guess = int(input('Your number: '))
    if guess < number: 
        print('Your number is smaller')
    elif guess > number:
        print('Your number is bigger')
    elif guess == number:
        break
print('You won! :)') 