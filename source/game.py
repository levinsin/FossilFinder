from engine import GameEngine, LetterGuessedError, InvalidGuessError

def main():

    game = GameEngine("wordrepo.txt")

    for _ in range(10):
        game.next_round()

        while True:
            
            guess = input("Enter your guess: ")
            try:
                game.make_guess(guess)
            except (InvalidGuessError, LetterGuessedError) as e:
                print(e)
                continue
            
            game.print_status()

            if game.word_guessed():
                print("Congratulations! You've guessed the word!")
                break

            elif game.failed():
                game.print_fail_message()
                break
            
        action = input("Do you want to continue guessing? (y/n): ")
        if action.lower() != 'y':
            break

        input("Press Enter to continue...")



if __name__ == "__main__":
    main()