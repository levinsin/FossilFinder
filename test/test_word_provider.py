"""Unit tests for the WordProvider class."""

import unittest
import os
import sys

from source.word_provider import WordProvider

# root path appended
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


class TestWordProvider(unittest.TestCase):
    """Test cases for the WordProvider class."""

    def setUp(self) -> None:
        """Set up test fixtures before each test method."""

        self.provider = WordProvider("wordrepo.txt")

    def test_init_with_valid_file(self) -> None:
        """Test initialization with a valid file."""

        self.assertEqual(len(self.provider.words), 10)

    def test_get_random_word(self) -> None:
        """Test getting a random word."""

        # saving the words before removal
        word_set = self.provider.words.copy()

        word = self.provider.get_random_word()

        self.assertIn(word, word_set)
        self.assertNotIn(word, self.provider.words)

    def test_get_random_word_empty_provider(self) -> None:
        """Test getting a word from an empty provider."""

        self.provider.words = set()

        with self.assertRaises(ValueError):
            self.provider.get_random_word()


if __name__ == "__main__":
    unittest.main()
