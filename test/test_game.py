"""This module contains unit tests for the game loop in source.game."""

import unittest
import sys
import os
from unittest.mock import patch

from source.engine import GameEngine, InvalidGuessError, LetterGuessedError

# append project root to path (source is a package now)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


class TestGameLoop(unittest.TestCase):
    """Test the game loop and the connection with the game engine."""

    def setUp(self) -> None:
        """Set up test mock objects."""

        with (
            patch("source.engine.UICreator"),
            patch("source.engine.WordProvider") as mock_word_provider,
        ):
            mock_word_provider.return_value.get_random_word.return_value = (
                "testword"
            )
            self.engine = GameEngine("test_words.txt")

    def test_engine_init(self) -> None:
        """Test that GameEngine is initialized correctly."""

        self.assertIsInstance(self.engine, GameEngine)
        self.assertEqual(self.engine.rounds, 0)
        self.assertEqual(self.engine.misses, 0)

    def test_invalid_guess(self) -> None:
        """Test that invalid guess raises InvalidGuessError."""

        self.engine.current_word = "test"

        with self.assertRaises(InvalidGuessError):
            self.engine.make_guess("a@b")

    def test_repeated_guess(self) -> None:
        """Test that repeated guess raises LetterGuessedError."""

        self.engine.current_word = "test"

        self.engine.make_guess("t")

        with self.assertRaises(LetterGuessedError):
            self.engine.make_guess("t")

    def test_failed_after_six_misses(self) -> None:
        """After 6 wrong guesses, the game should be failed."""

        self.engine.current_word = "test"

        wrong_letters = ["z", "q", "x", "j", "k", "w"]
        for letter in wrong_letters:
            self.engine.make_guess(letter)

        self.assertTrue(self.engine.failed())
        self.assertEqual(self.engine.misses, 6)

    def test_game_win_condition(self) -> None:
        """Test that game detects a win."""

        self.engine.current_word = "test"

        self.engine.make_guess("t")
        self.engine.make_guess("e")
        self.engine.make_guess("s")

        self.assertTrue(self.engine.word_guessed())
        self.assertFalse(self.engine.failed())

    def test_game_lose_condition(self) -> None:
        """Test that game detects a loss."""
        self.engine.current_word = "test"

        wrong_letters = ["z", "q", "x", "j", "k", "w"]
        for letter in wrong_letters:
            self.engine.make_guess(letter)

        self.assertTrue(self.engine.failed())
        self.assertFalse(self.engine.word_guessed())


if __name__ == "__main__":
    unittest.main()
