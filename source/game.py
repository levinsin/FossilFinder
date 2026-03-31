"""
This is the main file of the project.
It contains the game loop and connects with the GameEngine class.
"""

from source.engine import GameEngine, LetterGuessedError, InvalidGuessError


def main() -> None:
    """In the main function, the game loop runs."""

    engine: GameEngine = GameEngine("wordrepo.txt")

    while True:
        if not engine.next_round():
            engine.print_game_history()
            break

        while True:
            guess: str = str(input("Enter your guess: "))
            try:
                engine.make_guess(guess)
            except (InvalidGuessError, LetterGuessedError):
                continue

            engine.print_status()

            if engine.word_guessed():
                engine.save_game()
                print("Congratulations! You've guessed the word!")
                break

            if engine.failed():
                engine.save_game()
                engine.print_fail_message()
                break

        action = input("Do you want to continue guessing? (y/n): ")
        if action.lower() != "y":
            engine.print_game_history()
            break

        engine.creator.clear_screen()

        input("Press Enter to continue...")

        engine.creator.clear_screen()


if __name__ == "__main__":
    main()
