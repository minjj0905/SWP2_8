from hangman import Hangman
from guess import Guess
from word import Word
from termcolor import colored
import string


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())

    finished = False
    hangman = Hangman()

    while hangman.remainingLives > 0:

        display = hangman.currentShape()
        print(display)
        guess.displayCurrent()
        print("used letter: ")
        print()
        for i in string.ascii_lowercase:
            if i in guess.guessedChars:
                print(colored(i, 'red'), end=' ')
            else:
                print(colored(i, 'green'), end=' ')
        print()
        print()

        guessedChar = input('Select a letter: ')
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue

        success = guess.guess(guessedChar)
        print(success)
        if not success:
            hangman.decreaseLife()
        if guess.finished():
            break

    if guess.finished():
        print(guess.displayCurrent())
        print('Success')
    else:
        print(hangman.currentShape())
        print(guess.secretWord)
        guess.displayCurrent()
        print('Fail')


if __name__ == '__main__':
    gameMain()
