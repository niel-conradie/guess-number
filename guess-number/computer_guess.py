from random import randint


class ComputerGuess:
    """A class to represent a computer guess game."""

    @staticmethod
    def user_input():
        """Requesting user input and validating number."""
        while True:
            try:
                user_input = int(input("\nSelect a number to guess: "))
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
    def computer_guess(number):
        """Computer guess the number."""
        low = 1
        high = number
        guess = 0
        user_input = ""
        while user_input != "c":
            if low != high:
                guess = randint(low, high)
            else:
                guess = low

            # Requesting user input and validating choice.
            while True:
                user_input = input(
                    f"\nIf {guess} is correct then type 'C',"
                    "\ntoo low 'L', and too high 'H': "
                ).lower()

                choices = ["c", "l", "h"]
                if user_input in choices:
                    break
                else:
                    print(f"\n{user_input} is not an valid choice!")
                    continue

            # User input conditions.
            if user_input == "h":
                high = guess - 1
            elif user_input == "l":
                low = guess + 1

        print(f"\nThe computer have guessed the number {guess} correctly!")

    def start_game(self):
        """Starting computer guess game."""
        # Requesting user input.
        user_input = self.user_input()
        # Computer guess the number.
        self.computer_guess(user_input)
