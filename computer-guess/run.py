from computer_guess import ComputerGuess


def run():
    """ Computer Guess. """
    run = ComputerGuess()

    while True:
        # Requesting user input.
        user_input = run.user_input()
        # Computer guess the number.
        run.computer_guess(user_input)
        # Add point to the computer score.
        run.add_computer_score()
        # Display the scoreboard.
        run.display_scoreboard()
        # Requesting user input.
        run.restart()

        continue


if __name__ == "__main__":
    run()
