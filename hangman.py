import words
from random import choice

class Hangman():
    """Game Hangman"""

    def __init__(self):
        """Initialize attributes of game."""
        self.words = list(words.woorden.split(", "))
        self.lives = 5
        self.used_letters = []

    def generate_word(self):
        """Genetare random word from vakebulary."""
        self.word = choice(self.words)
        self.len_letters = len(list(self.word))
        print("The word has " + str(self.len_letters) + " letters.")
        print(self.word)
        return self.word
        return self.len_letters

    def guess_letter(self, letter):
        """Checking chosen letters (in word)?"""
        if letter:
            if letter in self.used_letters:
                print("You have already used this letter.")
            else:
                self.used_letters.append(letter)
                u_l = ' '.join(str(letter) for letter in self.used_letters)
                print("Used letters:")
                print(u_l)
                if letter in list(self.word):
                    self.position = self.word.index(letter)
                    if self.position + 1 == 1:
                        print("This is the 1'st letter of the word.")
                    elif self.position + 1 == 2:
                        print("This is the 2'nd letter of the word.")
                    elif self.position + 1 == 3:
                        print("This is the 3'rd letter of the word.")
                    elif self.position + 1  > 3:
                        self.position = self.position + 1
                        print("This is the " + str(self.position) + "'th letter of the word.")

                    return letter

                if letter not in list(self.word):
                    self.lives -= 1

    def add_guessed_letter(self):
        """Fill the empty spaces of word with guessed letters."""
        self.empty_word = "_"*len(list(self.word))
        self.empty_word = list(self.empty_word)
        print(len (self.empty_word))
        if self.empty_word[int(self.position)] > int(len(self.word)):
            self.empty_word[-1] = letter
        else:
            self.empty_word[self.position] = letter
        return self.empty_word

    def show_word(self):
        """Show the word."""
        self.guessed_word = self.empty_word
        print(self.guessed_word)

if __name__ == '__main__':
    i = Hangman()
    i.generate_word()
    while i.lives >0:
        letter = input("Choose the letter: ")
        i.guess_letter(letter)
        i.add_guessed_letter()
        i.show_word()
