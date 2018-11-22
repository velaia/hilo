import random
from typing import Any, Union


def main():
    success: bool = False
    result: int = random.randint(1, 100)
    print(f'Welcome to the HI - LO game!')

    while success is not True:
        guess_orig = input('Guess a number between 1 & 100: ')
        try:
            guess = int(guess_orig)
        except ValueError:
            print(f'No integer given: {guess_orig}')
            continue
        if guess == result:
            success = True
            print(f'Got it! The bumer is {result}')
        elif guess > result:
            print(f'Too high!')
        else:
            print(f'Too low!')


if __name__ == '__main__':
    main()
