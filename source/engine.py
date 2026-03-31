"""
Game engine class manages the game processes,
like the guess handling, game status or the history.

It connects the other classes WordProvider and UICreator.
"""

from source.word_provider import WordProvider
from source.ui_creator import UICreator

MAX_ROUNDS = 10


class InvalidGuessError(Exception):
    """
    Custom exception class for handling wrong inputs from the user.
    """


class LetterGuessedError(Exception):
    """
    Custom exception class for case when letter has already been guessed.
    """


class GameEngine:  # pylint: disable=too-many-instance-attributes
    """
    Game engine class manages the game processes,
    like the guess handling, game status and history.

    It connects both classes, the WordProvider and
    the UICreator classes (and the exception classes).
    """

    def __init__(self, file_path: str) -> None:

        # UI class
        self.creator: UICreator = UICreator()

        # guessed letters
        self.correct_guesses: set = set()
        self.wrong_guesses: set = set()

        # game variables
        self.rounds: int = 0
        self.game_history: dict = {}
        self.misses: int = 0
        self.current_word: str = ""
        self.word_provider: WordProvider = WordProvider(file_path)

    def next_round(self) -> bool:
        """
        This method handles the start of a new round.
        Some variables are reset and a new word is picked.
        """
        self.rounds += 1

        if self.rounds > MAX_ROUNDS:
            return False

        self.misses = 0

        try:
            self.current_word = self.word_provider.get_random_word()
        except ValueError:
            return False

        self.correct_guesses.clear()
        self.wrong_guesses.clear()

        return True

    def make_guess(self, guess: str) -> None:
        """
        This method handles the input of the user.
        The input is validated and the game state is updated.
        """

        self.creator.clear_screen()

        # Validate guess: must be alphabetic
        if not guess or not all(c.isalpha() or c.isspace() for c in guess):
            self.creator.display_status(
                word=self.current_word,
                mistakes=self.misses,
                wrong_letters=list(self.wrong_guesses),
                correct_letters=list(self.correct_guesses),
            )
            self.creator.print_invalid_guess(guess)
            raise InvalidGuessError("Guess must contain only letters.")

        # guessing a whole word
        if len(guess) > 1:
            if guess.lower() == self.current_word.lower():
                # correct guess -> direct win
                self.correct_guesses.update(set(guess.lower()))

            else:
                # wrong guess
                self.misses += 1
            return

        # single letter guessed
        guess = guess.lower()

        # check if letter has been guessed
        if guess in (self.correct_guesses | self.wrong_guesses):
            self.creator.display_status(
                word=self.current_word,
                mistakes=self.misses,
                wrong_letters=list(self.wrong_guesses),
                correct_letters=list(self.correct_guesses),
            )

            self.creator.print_letter_guessed(guess)
            raise LetterGuessedError("Letter has already been guessed.")

        # check if letter is in word
        if guess not in self.current_word.lower():
            self.wrong_guesses.add(guess)
            self.misses += 1
        else:
            self.correct_guesses.add(guess)

    def print_status(self) -> None:
        """
        Method prints the current game status.
        Therefore some information is passed to the UICreator class to display it.
        """

        self.creator.display_status(
            word=self.current_word,
            mistakes=self.misses,
            wrong_letters=list(self.wrong_guesses),
            correct_letters=list(self.correct_guesses),
        )

    def word_guessed(self) -> bool:
        """
        Method checks if the entire word has been guessed.
        """

        for letter in self.current_word.lower():
            if letter not in self.correct_guesses:
                return False

        return True

    def save_game(self) -> None:
        """
        Current game state is saved in the game history.
        """

        self.game_history[self.rounds] = self.misses, self.current_word

    def failed(self) -> bool:
        """
        Method returns if the user has failed in this round.
        """

        return self.misses >= 6

    def print_fail_message(self) -> None:
        """
        Method prints the fail message.
        """

        print(f"Game Over! The word was: {self.current_word}.")

    def print_game_history(self) -> None:
        """
        Method prints the game history.
        """

        print("\nGame History:")
        for round_num, (misses, word) in self.game_history.items():
            print(f"Round {round_num}: Word = '{word}', Mistakes = {misses}")
