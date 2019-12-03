class Hangman:

    def __init__(self):
        self.figure = [

            '''\
               ____
              |    |
              |    o
              |   /|\\
              |    |
              |   / \\
             _|_
            |   |______
            |          |
            |__________|\
            ''',

            '''\
               ____
              |    |
              |    o
              |   /|\\
              |    |
              |   /
             _|_
            |   |______
            |          |
            |__________|\
            ''',

            '''\
               ____
              |    |
              |    o
              |   /|\\
              |    |
              |
             _|_
            |   |______
            |          |
            |__________|\
            ''',

            '''\
               ____
              |    |
              |    o
              |   /|
              |    |
              |
             _|_
            |   |______
            |          |
            |__________|\
            ''',

            '''\
               ____
              |    |
              |    o
              |    |
              |    |
              |
             _|_
            |   |______
            |          |
            |__________|\
            ''',

            '''\
               ____
              |    |
              |    o
              |
              |
              |
             _|_
            |   |______
            |          |
            |__________|\
            ''',

            '''\
               ____
              |    |
              |
              |
              |
              |
             _|_
            |   |______
            |          |
            |__________|\
            ''',

        ]
        self.remainingLives = len(self.figure) - 1


    def decreaseLife(self):
        self.remainingLives -= 1

    def currentShape(self):
        return self.figure[self.remainingLives]
