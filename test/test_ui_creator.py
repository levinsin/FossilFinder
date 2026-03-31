"""Unit test for the UICreator class."""

import unittest
import sys
import os
from unittest.mock import patch

from source.ui_creator import UICreator

# append project root to path (source is a package now)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


class TestUICreator(unittest.TestCase):
    """Test cases for the UICreator class."""

    def setUp(self) -> None:
        """Set up test fixtures before each test method."""

        self.ui = UICreator()

    def test_display_status_basic(self) -> None:
        """Test basic display_status functionality."""

        with patch("builtins.print") as mock_print:
            self.ui.display_status(
                word="test", mistakes=0, wrong_letters=[], correct_letters=[]
            )

            # prints more than 5 lines
            self.assertGreater(mock_print.call_count, 5)

    def test_display_status_health_bar_green(self) -> None:
        """Test display_status with green health bar."""

        with patch("builtins.print") as mock_print:
            self.ui.display_status(
                word="test",
                mistakes=2,
                wrong_letters=["a", "b"],
                correct_letters=["t", "e"],
            )

            mock_print.assert_any_call(
                f"{self.ui.BLUE}║{self.ui.RESET}  Health:      "
                f"{self.ui.GREEN}[████████░░░░]{self.ui.RESET} 4/6 HP        "
                f"{self.ui.BLUE}║{self.ui.RESET}"
            )

    def test_display_status_health_bar_red(self) -> None:
        """Test display_status with red health bar."""

        with patch("builtins.print") as mock_print:
            self.ui.display_status(
                word="test",
                mistakes=5,
                wrong_letters=["a", "b", "c", "d", "e"],
                correct_letters=["t"],
            )

            mock_print.assert_any_call(
                f"{self.ui.BLUE}║{self.ui.RESET}  Health:      "
                f"{self.ui.RED}[██░░░░░░░░░░]{self.ui.RESET} 1/6 HP        "
                f"{self.ui.BLUE}║{self.ui.RESET}"
            )

    def test_display_status_word(self) -> None:
        """Test display_status the word display."""

        with patch("builtins.print") as mock_print:
            self.ui.display_status(
                word="test",
                mistakes=1,
                wrong_letters=["a"],
                correct_letters=["t", "e"],
            )

            lines = [call.args[0] for call in mock_print.call_args_list]
            word_lines = [line for line in lines if "Word:" in line]
            self.assertTrue(word_lines)
            self.assertIn("t e _ t", word_lines[0])

    def test_print_letter_guessed(self) -> None:
        """Test print_letter_guessed method."""

        with patch("builtins.print") as mock_print:
            self.ui.print_letter_guessed("a")

            mock_print.assert_called_once_with(
                f"{self.ui.YELLOW}You have already guessed 'a'.{self.ui.RESET}"
            )

    def test_print_invalid_guess(self) -> None:
        """Test print_invalid_guess method."""

        with patch("builtins.print") as mock_print:
            self.ui.print_invalid_guess("a@b")

            expected_message = (
                f"{self.ui.YELLOW}Invalid Guess 'a@b'. "
                f"Please enter a single letter.{self.ui.RESET}"
            )
            mock_print.assert_called_once_with(expected_message)


if __name__ == "__main__":
    unittest.main()
