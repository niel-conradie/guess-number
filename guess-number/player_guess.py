from random import randint


class PlayerGuess:
    """A class to represent a player guess game."""

    @staticmethod
    def user_input():
        """Requesting user input and validating number."""
        while True:
            try:
                user_input = int(input("\nSelect a range between 1 and "))
                if user_input == 0:
                    print("\nThat is not a valid number.")
                elif user_input < 0:
                    print("\nThat is a negative number.")
                else:
                    return user_input
            except ValueError:
                print("\nThat is not a number.")
                continue

    @staticmethod
    def random_number(user_input):
        """Randomly select a number between 1 and user input."""
        random_number = randint(1, user_input)
        return random_number

    @staticmethod
    def user_input_guess(user_input):
        """Requesting user input and validating number."""
        while True:
            try:
                user_input_guess = int(
                    input(f"\nGuess number between 1 and {user_input}: ")
                )
                return user_input_guess
            except ValueError:
                print("\nThat is not a number.")
                continue

    @staticmethod
    def correct_guess(user_input_guess, random_number):
        """Validating player guess conditions."""
        if user_input_guess < random_number:
            print("\nToo Low! Guess again.")
        elif user_input_guess > random_number:
            print("\nToo High! Guess again.")
        else:
            print("\nCongratulations!")
            print(f"\nYou have guessed the number {random_number} correctly!")

    def start_game(self):
        """Starting player guess game."""
        # Requesting user input.
        user_input = self.user_input()
        # Randomly select a number.
        random_number = self.random_number(user_input)

        user_input_guess = 0
        while user_input_guess != random_number:
            # Requesting user input.
            user_input_guess = self.user_input_guess(user_input)
            # Validating user input conditions.
            self.correct_guess(user_input_guess, random_number)
