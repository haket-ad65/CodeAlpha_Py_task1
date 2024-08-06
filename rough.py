import random

def hangman_game():
    print("*****The Hangman Game*****")
    
    # List of words
    word_list = ['apple', 'helicopter', 'codealpha', 'google', 'india', 'hockey', 'program', 'intern', 'youth', 'hoodie']
    word_chosen = random.choice(word_list).upper()
    hidden_word = list('_' * len(word_chosen))
    guessed_letters = set()
    num_attempts = 10
    
    # Function to display the current state of the word
    def display_hidden_word():
        print(' '.join(hidden_word))
    
    # Game loop
    while num_attempts > 0:
        display_hidden_word()
        guess = input("Guess a letter: ").upper()
        
        if guess in guessed_letters:
            print(f"You've already guessed {guess}. Try another letter.")
        elif guess in word_chosen:
            print(f'Yay!!! Correct guess: {guess}')
            for i, letter in enumerate(word_chosen):
                if letter == guess:
                    hidden_word[i] = guess
        else:
            num_attempts -= 1
            print(f'Oops! No {guess} in the hidden word. {num_attempts} attempts left.')
        
        guessed_letters.add(guess)
        
        if '_' not in hidden_word:
            print(f'\nCongrats!!!! You win! The hidden word was: {word_chosen}')
            break
    else:
        print(f'\nSorry, You lose. The hidden word was: {word_chosen}')

# Run the game
hangman_game()
