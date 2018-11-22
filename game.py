import random


def main():
    success: bool = False
    print(f'Welcome to the HI - LO game!')
    result = random.randint(1, 100)

    while success is not True:
        guess = input('Guess a number between 1 & 100: ')
        guess = int(guess)
        if guess == result:
            success = True
            print(f'Got it! The bumer is {result}')
        elif guess > result:
            print(f'Too high!')
        else:
            print(f'Too low!')


if __name__ == '__main__':
    main()
