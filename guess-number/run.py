from sys import exit

from number_guess import NumberGuess


def run():
    """Number Guess."""
    run = NumberGuess()

    try:
        # Starting the game.
        run.start_game()
    except KeyboardInterrupt:
        # Stopping the game.
        exit("\n\nProgram Terminated")


if __name__ == "__main__":
    run()
