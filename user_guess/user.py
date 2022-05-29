import random


def user_guess(number):
    """ User guess the number. """
    random_number = random.randint(1, number)

    player_input = 0
    while player_input != random_number:
        # Requesting player input.
        player_input = int(
            input(f"\nGuess the number between 1 and {number}: "))

        # Too Low/High player input conditions.
        if player_input < random_number:
            print("\nToo Low! Guess again.")
        elif player_input > random_number:
            print("\nToo High! Guess again.")

    print("\nCongratulations!")
    print(f"You have guessed the number {random_number} correctly!")


def play():
    """ Guess the number. """
    # Requesting player input.
    player_input = int(input("Pick a range between 1 and "))

    # Passing player input as argument.
    user_guess(player_input)


if __name__ == "__main__":
    play()
