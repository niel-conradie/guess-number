import random


def computer_guess(number):
    """ Computer guess the number. """
    low = 1
    high = number
    player_input = ''
    while player_input != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        # Requesting player input.
        player_input = input(f"\nIf {guess} is correct then type 'C',\n"
                             f"too low 'L', and too high 'H': ").lower()

        # Player input conditions.
        if player_input == 'h':
            high = guess - 1
        elif player_input == 'l':
            low = guess + 1

    print(f"\nThe computer have guessed the number {guess} correctly!")


def play():
    """ Guess the number. """
    # Requesting player input.
    player_input = int(input("Pick a number to guess: "))

    # Passing player input as argument.
    computer_guess(player_input)


if __name__ == '__main__':
    play()
