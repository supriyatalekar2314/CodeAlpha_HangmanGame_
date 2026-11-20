import random

# List of words
words = ["apple", "mango", "banana", "school", "flower"]

print("================================")
print("       HANGMAN GAME")
print("================================")

# Play again loop
while True:

    word = random.choice(words)

    guessed_letters = []
    wrong_guesses = 0
    max_attempts = 6

    # Game starts
    while wrong_guesses < max_attempts:

        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Wrong attempts:", wrong_guesses, "/", max_attempts)

        # Check winning condition
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You Won!")
            break

        # Take user input
        guess = input("Guess one letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet!")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter!")
            continue

        guessed_letters.append(guess)

        # Check letter
        if guess in word:
            print("Correct Guess!")
        else:
            wrong_guesses += 1
            print("Wrong Guess!")

    # Losing condition
    if wrong_guesses == max_attempts:
        print("\nGame Over!")
        print("Correct word was:", word)

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thank you for playing!")
        break