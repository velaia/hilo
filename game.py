import random


def main():
    """Main function with loop for hi-lo game.

    :return: None
    """
    result: int = random.randint(1, 100)
    print(f'Welcome to the HI - LO game!')

    while True:
        guess_orig = input('Guess a number between 1 & 100: ')
        try:
            guess = int(guess_orig)
        except ValueError:
            print(f'No integer given: {guess_orig}')
            continue
        if guess == result:
            print(f'Got it! The number is {result}')
            break
        elif guess > result:
            print(f'Too high!')
        else:
            print(f'Too low!')


if __name__ == '__main__':
    main()
