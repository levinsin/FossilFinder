"""
WordProvider class fetches words from the file and picks every time a random word.
It makes sure that one word can only be picked once.
"""

import random
import os


class WordProvider: # pylint: disable=too-few-public-methods
    """
    This class fetches words from the file. It contains a method to get a random word
    and makes sure that one word cannot be picked twice.
    """

    def __init__(self, file_name: str) -> None:
        directory_path: str = os.path.dirname(os.path.abspath(__file__))

        with open(
            os.path.join(
                directory_path, file_name), "r", encoding="utf-8"
            ) as file:
            self.words: set[str] = {
                line.strip() for line in file if line.strip()
            }

    def get_random_word(self) -> str:
        """
        This method picks a random word from the set.
        When no words are left, a ValueError is raised.
        """

        if not self.words:
            raise ValueError("No words available in the provider.")

        picked_word: str = str(random.choice(list(self.words)))
        self.words.remove(picked_word)

        return picked_word
