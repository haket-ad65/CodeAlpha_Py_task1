# Creating a Hangman game using python
import random
def hangman_game():
    print("*****The Hangman Game*****")
# number of words using list
    word_list=['apple','helicopter','codealpha','google','india','hockey','program','intern', 'youth','hoddie','monday','mother','semester']
    word_chosen=random.choice(word_list).upper()
    hidden_word =list('_'*len(word_chosen))
    letter_guess=set()
    num_count=10
# function for hidden word
    def display_hidden_word():
     print(''.join(hidden_word))
# using while loop for counting failed attempt
    while num_count>0:
        display_hidden_word()
        guess=input("").upper()

        if guess in word_chosen:
            print(f'yay!!! correct guess :-) more {guess} in the hidden word!')
            for i, letter in enumerate(word_chosen):
               if letter == guess:
                  hidden_word[i] = guess
        elif guess in letter_guess:
          print(f"Already guessed{guess} try another letter !!!")
        else:
            num_count-=1
            print(f'oops! there are no {guess} in the Hidden word :-( ')
            print(f'{num_count} turn left')

        letter_guess.add(guess)

        if '_' not in hidden_word:
            print('congrats!!! You are the winner')
            print(f'the hidden word was {word_chosen}')
    else:
        print(f'the hidden word was {word_chosen}')
        print('Sorry You lose!!! better luck next time')

# deploying the game
hangman_game()