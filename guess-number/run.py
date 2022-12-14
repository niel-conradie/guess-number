from number_guess import NumberGuess


def run():
    """Number Guess."""
    run = NumberGuess()

    try:
        # Starting the game.
        run.start_game()
    except KeyboardInterrupt:
            # Stop the game.
            print("\n\nProgram Terminated")
            pass


if __name__ == "__main__":
    run()
