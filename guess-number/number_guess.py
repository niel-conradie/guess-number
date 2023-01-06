from computer_guess import ComputerGuess
from player_guess import PlayerGuess


class NumberGuess:
    """A class to represent a number guess game."""

    def __init__(self):
        """Initialize class attributes."""
        self.score = 0

    @staticmethod
    def user_input():
        """Requesting user input and validating choice."""
        while True:
            # Display user input options.
            print("\nSelect your game mode.")
            print("\nComputer Guess: Type '1'")
            print("Player Guess: Type '2'")

            # Requesting user input.
            try:
                user_input = int(input("\nEnter: "))
            except ValueError:
                print("\nThat is not a number.")
                continue

            # User input validation conditions.
            choices = [1, 2]
            if user_input not in choices:
                print(f"\n{user_input} is not an valid choice!")
                continue
            elif user_input == 1:
                return ComputerGuess()
            elif user_input == 2:
                return PlayerGuess()

    def add_score(self):
        """Add point to the scoreboard."""
        self.score += 1

    def scoreboard(self):
        """Display the amount of correct answers."""
        print(f"Correct: {self.score}")

    def start_game(self):
        """Starting number guess game."""
        while True:
            # Requesting user input.
            user_input = self.user_input()

            while True:
                # Starting the appropriate game mode.
                user_input.start_game()
                # Correct guess.
                self.add_score()
                self.scoreboard()
                # Requesting user input.
                self.restart()

    @staticmethod
    def restart():
        """Requesting user input and validating choice."""
        while True:
            # Display user input options.
            print("\nPlay Again?")
            print("\nYes: Type '1'")
            print("No: Type '2'")

            # Requesting user input.
            try:
                user_input = int(input("\nEnter: "))
            except ValueError:
                print("\nThat is not a number.")
                continue

            # User input validation conditions.
            choices = [1, 2]
            if user_input not in choices:
                print(f"\n{user_input} is not an valid choice!")
                continue
            elif user_input == 1:
                return
            elif user_input == 2:
                quit("\nThank you for playing!")
