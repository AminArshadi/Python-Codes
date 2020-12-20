from random import randint


def guess():
    value = randint(1, 10)
    number = int(input('Guess the secret number ( You have only three guesses!): '))
    guess = 0

    while True:
        guess = guess + 1
        if number > value and guess < 3:
            print('Your guess was too high!')
            number = int(input('Guess the secret number again: '))
        elif number < value and guess < 3:
            print('Your guess was too low!')
            number = int(input('Guess the secret number again: '))
        elif number == value and guess < 3:
            print('You got it right! You found the secret number in ' + str(guess) + ' guess(es).')
            break
        elif guess == 3:
            print('Game over!')
            break
