"""
The UICreator class manages most of the user interface of the game.
This includes the display of the game status, the health bar,
and messages for invalid guesses or already guessed letters.
"""

import os

class UICreator:
    """
    UICreator class is responsible for displaying 
    the game status and messages to the user.
    """

    # constants for class
    HEADER: str = "\033[95m"
    BLUE: str = "\033[94m"
    CYAN: str = "\033[96m"
    GREEN: str = "\033[92m"
    YELLOW: str = "\033[93m"
    RED: str = "\033[91m"
    BOLD: str = "\033[1m"
    RESET: str = "\033[0m"

    MAX_TRIES: int = 6

    def display_status(self, word: str, mistakes: int,
                       wrong_letters: list, correct_letters: list) -> None:
        """
        Displays the current game status in a card format. 
        Informations from the game engine class are passed.
        """

        # ==== Table Header ====
        print(
            f"\n{self.BLUE}╔══════════════════════" \
            f"══════════════════════╗{self.RESET}"
        )

        title: str = "FossilFinder v1.0"

        # ==== Title ====
        print(
            f"{self.BLUE}║{self.BOLD}{self.CYAN}" \
            f"{title: ^44}{self.BLUE}║{self.RESET}"
        )
        print(
            f"{self.BLUE}╠════════════════════════" \
            f"════════════════════╣{self.RESET}"
        )

        # ==== Health Bar ====
        bar_length: int = 12
        filled: int = int((self.MAX_TRIES - mistakes) /
                     self.MAX_TRIES * bar_length)

        health_bar: str = "█" * filled + "░" * (bar_length - filled)

        color: str = self.GREEN if (self.MAX_TRIES - mistakes) > 3 else self.RED

        health: str = f"{color}[{health_bar}]{self.RESET} " \
                 f"{self.MAX_TRIES - mistakes}/{self.MAX_TRIES} HP"

        print(
            f"{self.BLUE}║{self.RESET}  Health: " \
            f"{health: ^41}  {self.BLUE}║{self.RESET}"
        )

        # ==== Word Display ====
        spaced_word: str = ""
        for letter in word:
            if letter.lower() in correct_letters:
                spaced_word += letter + " "
            else:
                spaced_word += "_ "
        print(
            f"{self.BLUE}║{self.RESET}  Word: " \
            f"{self.BOLD}{spaced_word: ^34}{self.RESET} " \
            f" {self.BLUE}║{self.RESET}"
        )

        # ==== Wrong Letters ====
        letters_found: str = " ".join(sorted(wrong_letters)) if wrong_letters else "---"
        wrong_str: str = f"{self.RED}[{letters_found}]{self.RESET}"
        print(
            f"{self.BLUE}║{self.RESET}  Wrong Letters: " \
            f"{wrong_str: ^34}  {self.BLUE}║{self.RESET}"
        )

        print(
            f"{self.BLUE}╚══════════════════════════" \
            f"══════════════════╝{self.RESET}"
        )


    def clear_screen(self) -> None:
        """Clears the screen of the terminal for better readability."""

        os.system("cls" if os.name == "nt" else "clear")


    def print_letter_guessed(self, letter: str) -> None:
        """Prints a message when a letter has already been guessed."""

        print(f"{self.YELLOW}You have already guessed '{letter}'.{self.RESET}")


    def print_invalid_guess(self, guess: str) -> None:
        """Prints an error message for an invalid user guess."""

        print(
            f"{self.YELLOW}Invalid Guess '{guess}'. " \
            f"Please enter a single letter.{self.RESET}"
        )
