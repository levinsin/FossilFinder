"""Unit tests for the GameEngine class."""

import unittest
import sys
import os
from unittest.mock import patch

from source.engine import GameEngine, InvalidGuessError, LetterGuessedError

# append project root to the path (not required once source is a package)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


class TestGameEngine(unittest.TestCase):
    """Test cases for the GameEngine class."""

    def setUp(self) -> None:
        """Set up test fixtures before each test method."""

        with (
            patch("source.engine.UICreator") as mock_ui,
            patch("source.engine.WordProvider") as mock_word_provider,
        ):
            self.mock_ui = mock_ui.return_value
            self.mock_word_provider = mock_word_provider.return_value
            self.mock_word_provider.get_random_word.return_value = "testword"

            # game engine instance
            self.engine = GameEngine("test_words.txt")

    def test_init(self) -> None:
        """Test engine initialization."""

        self.assertEqual(self.engine.rounds, 0)
        self.assertEqual(self.engine.misses, 0)
        self.assertEqual(len(self.engine.correct_guesses), 0)
        self.assertEqual(len(self.engine.wrong_guesses), 0)
        self.assertEqual(len(self.engine.game_history), 0)
        self.assertEqual(self.engine.current_word, "")

    def test_next_round_first_round(self) -> None:
        """Test first round of game engine."""

        result = self.engine.next_round()

        self.assertTrue(result)
        self.assertEqual(self.engine.rounds, 1)
        self.assertEqual(self.engine.misses, 0)
        self.assertEqual(self.engine.current_word, "testword")
        self.mock_word_provider.get_random_word.assert_called_once()

    def test_next_round_max_rounds(self) -> None:
        """
        Test if engine returns false when the current
        round is greather than the maximum rounds allowed.
        """

        self.engine.rounds = 10

        result = self.engine.next_round()

        self.assertFalse(result)
        self.assertEqual(self.engine.rounds, 11)

    def test_next_round_no_words(self) -> None:
        """Test that next_round raises ValueError when no words are left."""

        self.mock_word_provider.get_random_word.side_effect = ValueError

        self.assertFalse(self.engine.next_round())

    def test_make_guess_word(self) -> None:
        """Test guessing word completely."""

        self.engine.current_word = "airbus"

        self.engine.make_guess("airbus")

        self.assertEqual(len(self.engine.correct_guesses), 6)
        self.assertEqual(len(self.engine.wrong_guesses), 0)
        self.assertEqual(self.engine.misses, 0)

    def test_make_guess_word_wrong(self) -> None:
        """Test guessing a wrong word."""

        self.engine.current_word = "airbus"

        self.engine.make_guess("boeing")

        self.assertEqual(len(self.engine.correct_guesses), 0)
        self.assertEqual(len(self.engine.wrong_guesses), 0)
        self.assertEqual(self.engine.misses, 1)

    def test_make_guess_empty(self) -> None:
        """Test making guess with space in it."""

        self.engine.current_word = "python"

        with self.assertRaises(InvalidGuessError):
            self.engine.make_guess("")

    def test_make_guess_symbol(self) -> None:
        """Test making guess with symbol in it."""

        self.engine.current_word = "trex"

        with self.assertRaises(InvalidGuessError):
            self.engine.make_guess("t-rex")

    def test_make_guess_letter_correct(self) -> None:
        """Test guessing a correct letter."""
        self.engine.current_word = "testword"

        self.engine.make_guess("t")

        self.assertIn("t", self.engine.correct_guesses)
        self.assertEqual(len(self.engine.wrong_guesses), 0)
        self.assertEqual(self.engine.misses, 0)

    def test_make_guess_letter_wrong(self) -> None:
        """Test guessing a wrong letter."""

        self.engine.current_word = "testword"

        self.engine.make_guess("z")

        self.assertEqual(len(self.engine.correct_guesses), 0)
        self.assertIn("z", self.engine.wrong_guesses)
        self.assertEqual(self.engine.misses, 1)

    def test_make_guess_upper_case(self) -> None:
        """Test that guesses don't depend on their case."""

        self.engine.current_word = "TestWord"

        self.engine.make_guess("T")
        self.engine.make_guess("w")

        self.assertIn("t", self.engine.correct_guesses)
        self.assertIn("w", self.engine.correct_guesses)

    def test_make_guess_already_guessed_correct(self) -> None:
        """Test guessing a letter that was already guessed correctly."""

        self.engine.current_word = "testword"
        self.engine.correct_guesses.add("t")

        with self.assertRaises(LetterGuessedError):
            self.engine.make_guess("t")

    def test_make_guess_already_guessed_wrong(self) -> None:
        """Test guessing a letter that was already guessed incorrectly."""

        self.engine.current_word = "testword"
        self.engine.wrong_guesses.add("z")

        with self.assertRaises(LetterGuessedError):
            self.engine.make_guess("z")

    def test_word_guessed_true(self) -> None:
        """Test when word is completely guessed."""

        self.engine.current_word = "test"
        self.engine.correct_guesses = {"t", "e", "s"}

        self.assertTrue(self.engine.word_guessed())

    def test_word_guessed_false(self) -> None:
        """Test when word is not completely guessed."""

        self.engine.current_word = "test"
        self.engine.correct_guesses.update({"t", "e"})

        self.assertFalse(self.engine.word_guessed())

    def test_failed(self) -> None:
        """Test when game is failed."""

        self.engine.misses = 7

        self.assertTrue(self.engine.failed())

    def test_fail_message_output(self) -> None:
        """Test that fail message prints the correct word."""

        self.engine.current_word = "testword"

        with patch("builtins.print") as mock_print:
            self.engine.print_fail_message()
            mock_print.assert_called_once_with(
                "Game Over! The word was: testword."
            )

    def test_print_fail_message(self) -> None:
        """Test printing failure message."""

        self.engine.current_word = "testword"

        with patch("builtins.print") as mock_print:
            self.engine.print_fail_message()
            mock_print.assert_called_once_with(
                "Game Over! The word was: testword."
            )

    def test_print_game_history(self) -> None:
        """Test printing game history."""

        self.engine.game_history = {
            1: (2, "word1"),
            2: (0, "word2"),
            3: (5, "word3"),
        }

        with patch("builtins.print") as mock_print:
            self.engine.print_game_history()

            # 4 calls: header + 3 entries
            self.assertEqual(mock_print.call_count, 4)


if __name__ == "__main__":
    unittest.main()
