from computer_guess import ComputerGuess
from player_guess import PlayerGuess


class NumberGuess:
    """A class to represent a number guess game."""

    def __init__(self):
        """Initialize class attributes."""
        self.computer_score = 0
        self.player_score = 0

    @staticmethod
    def user_input():
        """Requesting user input and validating choice."""
        while True:
            try:
                user_input = int(input("Enter: "))
            except ValueError:
                print("\nThat is not a number.\n")
                continue

            choices = [1, 2]
            if user_input not in choices:
                print(f"\n{user_input} is not an valid choice!\n")
                continue
            else:
                return user_input

    @staticmethod
    def user_input_allocation(user_input):
        """Assign user input to appropriate game mode."""
        if user_input == 1:
            return ComputerGuess()
        if user_input == 2:
            return PlayerGuess()

    @staticmethod
    def display_options():
        """Display game mode options."""
        print("\nSelect your game mode.")
        print("\nComputer Guess: Type '1'")
        print("Player Guess: Type '2'\n")

    def add_computer_score(self):
        """Add point to the computer score."""
        self.computer_score += 1

    def computer_scoreboard(self):
        """Display the amount of correct answers."""
        print(f"Correct: {self.computer_score}")

    def add_player_score(self):
        """Add point to the player score."""
        self.player_score += 1

    def player_scoreboard(self):
        """Display the amount of correct answers."""
        print(f"Correct: {self.player_score}")

    def start_game(self):
        """Starting number guess game."""
        while True:
            # Display game mode options.
            self.display_options()
            # Requesting user input.
            user_input = self.user_input()
            # Assign player to appropriate game mode.
            mode = self.user_input_allocation(user_input)

            while True:
                # Starting the appropriate game mode.
                game = mode.start_game()

                # Correct computer guess condition.
                if game == "computer_guess":
                    self.add_computer_score()
                    self.computer_scoreboard()
                # Correct player guess condition.
                if game == "player_guess":
                    self.add_player_score()
                    self.player_scoreboard()

                # Requesting user input.
                self.restart()

    @staticmethod
    def restart():
        """Requesting user input and validating choice."""
        while True:
            user_input = input("\nRestart? Yes/No: ").lower()
            choices = ["yes", "no"]
            if user_input not in choices:
                print("\nPlease type 'yes' or 'no'")
                continue

            # User input conditions.
            if user_input == "yes":
                break
            if user_input == "no":
                print("\nThank you for playing!")
                quit()


if __name__ == "__main__":
    run = NumberGuess()

    # Starting the game.
    run.start_game()
