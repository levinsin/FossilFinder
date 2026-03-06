from word_provider import WordProvider

"""

"""
class InvalidGuessError(Exception):
    pass

"""
Custom exception class for case when letter has already been guessed.
"""
class LetterGuessedError(Exception):
    pass

"""

"""
class GameEngine:

    def __init__(self, file_path) -> None:
        
        self.rounds = 0
        self.game_history = dict()
        self.misses = 0
        self.current_word = None
        self.word_provider = WordProvider(file_path)
        

    def next_round(self):

        self.rounds += 1
        self.misses = 0
        self.current_word = self.word_provider.get_random_word()
        self.already_guessed = set()


    def make_guess(self, guess: str):

        # single letter and alphabetic
        if len(guess) != 1 or not guess.isalpha():
            raise InvalidGuessError("Guess must be a single letter.")

        guess = guess.lower()
        
        if guess in self.already_guessed:
            raise LetterGuessedError("Letter has already been guessed.")
        
        if guess not in self.current_word.lower():
            self.misses += 1
        self.already_guessed.add(guess)


    def print_status(self):
        
        for letter in self.current_word:
            if letter.lower() in self.already_guessed:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print(f"\nMisses: {self.misses}")


    def word_guessed(self) -> bool:
        for letter in self.current_word.lower():
            if letter not in self.already_guessed:
                return False
        
        self.game_history[self.rounds] = self.misses, self.current_word
        return True
    

    def failed(self) -> bool:
        return self.misses >= 7
    

    def print_fail_message(self):
        print(f"Game Over! The word was: {self.current_word}")
