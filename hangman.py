

import random

# Small list of 5 predefined words
words = ["python", "program", "hangman", "computer", "keyboard"]

MAX_WRONG = 6  # maximum incorrect guesses allowed


def show_status(display, wrong_guesses, guessed):
    """Print the current state of the game."""
    print("\nWord:", " ".join(display))
    print("Wrong guesses left:", MAX_WRONG - len(wrong_guesses))
    if len(wrong_guesses) > 0:
        print("Wrong letters:", ", ".join(wrong_guesses))


def play_game():
    # Pick a random word
    secret_word = random.choice(words)

    # List of underscores, one for each letter
    display = ["_"] * len(secret_word)

    guessed = []        # all letters guessed so far
    wrong_guesses = []  # only the incorrect letters

    print("=" * 30)
    print("     WELCOME TO HANGMAN!")
    print("=" * 30)
    print("Guess the word one letter at a time.")
    print("You can make", MAX_WRONG, "wrong guesses.")

    # Main game loop
    while len(wrong_guesses) < MAX_WRONG and "_" in display:
        show_status(display, wrong_guesses, guessed)

        guess = input("Enter a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
        elif guess in guessed:
            print("You already guessed '" + guess + "'. Try another.")
        else:
            guessed.append(guess)

            if guess in secret_word:
                print("Good guess! '" + guess + "' is in the word.")
                # Reveal every position where the letter appears
                for i in range(len(secret_word)):
                    if secret_word[i] == guess:
                        display[i] = guess
            else:
                print("Sorry, '" + guess + "' is not in the word.")
                wrong_guesses.append(guess)

    # Game over: check the result
    print("\nWord:", " ".join(display))
    if "_" not in display:
        print("Congratulations! You won! The word was '" + secret_word + "'.")
    else:
        print("Game over! You ran out of guesses. The word was '" + secret_word + "'.")


def main():
    play_again = "y"
    while play_again == "y":
        play_game()
        play_again = input("\nPlay again? (y/n): ").lower().strip()
    print("Thanks for playing!")


main()
