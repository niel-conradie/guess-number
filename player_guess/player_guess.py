import random


class PlayerGuess:
    """ A class to represent a guess game. """

    @staticmethod
    def user_input():
        """ Requesting user input and validating number. """
        while True:
            try:
                user_input = int(input("\nSelect a range between 1 and "))
                return user_input
            except ValueError:
                print(f"\nThat is not a number.")
                continue

    @staticmethod
    def random_number(user_input):
        """ Randomly select a number between 1 and user input. """
        random_number = random.randint(1, user_input)
        return random_number

    @staticmethod
    def user_input_guess(user_input):
        """ Requesting user input and validating number. """
        while True:
            try:
                user_input_guess = int(input(f"\nGuess number between 1 and {user_input}: "))
                return user_input_guess
            except ValueError:
                print(f"\nThat is not a number.")
                continue

    @staticmethod
    def correct_guess(user_input_guess, random_number):
        """ Validating player guess conditions. """
        if user_input_guess < random_number:
            print("\nToo Low! Guess again.")
        elif user_input_guess > random_number:
            print("\nToo High! Guess again.")
        else:
            print("\nCongratulations!")
            print(f"You have guessed the number {random_number} correctly!")
