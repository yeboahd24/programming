# This is a guess number game.
from random import randint

secretNumber = randint(1, 20)
display = "I'm thinking of a number between 1 and 20"
print(display)

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input('Your guess: '))

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break  # This condition is the correct guess!

if guess == secretNumber:
    print('God job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope.The number I was thinking of was ' + str(secretNumber))
