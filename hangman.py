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
                print(u_l)
                if letter in list(self.word):
                    return letter
                    return index(letter)

                if letter not in list(self.word):
                    self.lives -= 1

    def add_guessed_letter(self):
        """Fill the empty spaces of word with guessed letters."""
        self.empty_word = "_ "*len(list(self.word))
        self.empty_word = list(self.empty_word)
        for e in self.empty_word:
            e[self.word.index(letter)] = letter
            return self.empty_word

    def show_word(self):
        """Show the word."""
        self.guessed_word = self.empty_word
        print(self.guessed_word)


i = Hangman()
i.generate_word()
letter = input("Choose the letter: ")
i.guess_letter(letter)
i.add_guessed_letter()
i.show_word()
