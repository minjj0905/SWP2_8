from termcolor import colored
import string


class Guess:

    def __init__(self, word):
        self.word = word
        self.guessedChars = []
        self.numTries = 0
        self.foundChars = []

    def display(self):
        print('\n')
        self.currentList = ["▢"] * len(self.word)
        print("used letter: ")
        for i in string.ascii_lowercase:
            if i in self.guessedChars:
                print(colored(i, 'red'), end=' ')
            else:
                print(colored(i, 'green'), end=' ')
        print()
        print()
        for i, j in self.foundChars:
            self.currentList[j] = i
        print(" ".join(self.currentList))

    def guess(self, character):
        if character not in self.word:
            self.numTries += 1
        if character not in self.guessedChars:
            self.guessedChars.append(character)
            for i in range(len(self.word)):
                if character == self.word[i]:
                    self.foundChars.append((character, i))
        if len(self.foundChars) == len(self.word):
            return True
        else:
            return False


if __name__ == '__main__':
    G = Guess('apple')
    while True:
        char = input("Select a letter: ")
        if G.guess(char):
            break
        G.display()
    G.display()