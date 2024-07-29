# Word Guess Game

# Player 1 enters the word
word_to_guess = input("Enter the word you want the opponent to guess(not more than seven letters): ").lower()
print(f"The word has {len(word_to_guess)} letters.")

# Initialize variables
guessed_letters = set()
attempts_left = 15
display = '_' * len(word_to_guess)

print(display)

# Main game  loop
while attempts_left > 0:
    # Opponent guesses a etter
    guess = input("Guess a letter: ").lower()
    
    # Validate the guess
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please guess a single letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter. Try again.")
        continue

    # Add the guess to the set of guessed letters
    guessed_letters.add(guess)

    # Check if the guess is in the word
    if guess in word_to_guess:
        print("Good guess!")
    else:
        print("Try again.")
        attempts_left -= 1

    # Update the display with correctly guessed letters
    display = ''
    for letter in word_to_guess:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    print(display)

    # Check if the whole word is guessed
    if '_' not in display:
        print("Congratulations! You've guessed the word!")
        break
else:
    print(f"Sorry, you've run out of attempts. The word was '{word_to_guess}'.")
