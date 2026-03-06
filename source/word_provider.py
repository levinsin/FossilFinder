import random

"""
This class fetches words from the file. It contains a method to get a random word
and makes sure that one word cannot be picked twice.
"""
class WordProvider:

    def __init__(self, file_path):

        with open(file_path, 'r') as file:
            self.words = [line.strip() for line in file if line.strip()]

    def get_random_word(self):

        if not self.words:
            raise ValueError("No words available in the provider.")
        
        picked_word = random.choice(self.words)
        self.words.remove(picked_word) 

        return picked_word