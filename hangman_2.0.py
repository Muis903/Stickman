import words
from random import choice
import string
from hangman_visual import lives_visual_dict

def get_valid_word():

    word = choice(list(words.woorden.split(", ")))
    return word.upper()


def hangman():

    word = get_valid_word()
#___________________
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7


    while lives >0 and len(word_letters) >0:
        print("You have ", lives, " lives left and have used these letters: ", ' '.join(used_letters))
        # Get user input

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess the letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1
                print("\nYour letter:", user_letter, "is not in the word.")

        elif user_letter in used_letters:
            print("\nYou have already used this letter.")

        else:
            print("\nThat is mot an valid letter.")

    if lives == 0:
        print(lives_visual_dict[lives])
        print("You died. Sorry, the word was", word)

    else:
        print("\nYay! You win!!!\n" + "The word was", word)


hangman()
