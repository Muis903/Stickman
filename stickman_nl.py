import words
from random import choice

#Create an list with words to play with
words = list(words.woorden.split(", "))

#Create amount of lives

lives = 5
word = (choice(words))
letters = list(word)
used_letters = []
print("\n\t\t\t<---Word is chosen! Gues!--->\n")


while lives > 0:
    len_letters = len(letters)
    print("\nThe word has " + str(len(letters)) + " letters.\n")
    letter = input("\nChoose the letter:")

#Used letters 
    if letter:
        if letter in used_letters:
            print("You have already used this letter.")
            continue
        else:
            used_letters.append(letter)
            print("\nUsed letters:")
            u_l = ' '.join(str(letter) for letter in used_letters)
            print(u_l)

    if letter in letters:
        position = word.index(letter)

        if position + 1 == 1:
            print("This is the 1'st letter of the word.")
        elif position + 1 == 2:
            print("This is the 2'nd letter of the word.")
        elif position + 1 == 3:
            print("This is the 3'rd letter of the word.")
        elif position + 1  > 3:
            position = position + 1
            print("This is the " + str(position) + "'th letter of the word.")

    if letter not in letters:
        lives -= 1


    len_word = "_ "* int(len(word))
    len_word = list(len_word)
    print("\n"+ len_word)

