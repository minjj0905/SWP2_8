


class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.guessedChars = []
        self.foundChars = []

    def displayCurrent(self):
        self.currentList = ["▢"] * len(self.secretWord)
        for i, j in self.foundChars:
            self.currentList[j] = i
        print(" ".join(self.currentList))
        return self.currentList

    def displayGuessed(self):
        return self.foundChars

    def guess(self, character):
        if character not in self.guessedChars:
            self.guessedChars.append(character)
            for i in range(len(self.secretWord)):
                if character == self.secretWord[i]:
                    self.foundChars.append((character, i))
        return character in self.secretWord

    def finished(self):
        return len(self.foundChars) == len(self.secretWord)


if __name__ == '__main__':
    G = Guess('apple')
    while True:
        char = input("Select a letter: ")
        if G.guess(char):
            break
