from player_guess import PlayerGuess


def run():
    """Player Guess."""
    run = PlayerGuess()

    while True:
        # Requesting user input.
        user_input = run.user_input()
        # Randomly select a number.
        random_number = run.random_number(user_input)

        user_input_guess = 0
        while user_input_guess != random_number:
            # Requesting user input.
            user_input_guess = run.user_input_guess(user_input)
            # Validating user input conditions.
            run.correct_guess(user_input_guess, random_number)

        # Add point to the player score.
        run.add_player_score()
        # Display the scoreboard.
        run.display_scoreboard()
        # Requesting user input.
        run.restart()

        continue


if __name__ == "__main__":
    run()
