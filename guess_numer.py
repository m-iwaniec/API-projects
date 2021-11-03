import random


# player guesses

def guess_nr(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, too low! Guess again.')
        elif guess > random_number:
            print('Sorry, too high! Guess again.')

    print(f'Good job! You guessed the number {random_number}!!')


guess_nr(10)


# computer guesses

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Game over! The computer guessed your number, {guess}!')


computer_guess(55)
