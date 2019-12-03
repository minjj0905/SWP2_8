import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.g1.guess('e')
        self.assertEqual(self.g1.displayCurrent(), list('▢ e ▢ ▢ ▢ ▢ ▢'.split(' ')))
        self.assertFalse(self.g1.finished())
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), list('▢ e ▢ a ▢ ▢ ▢'.split(' ')))
        self.assertFalse(self.g1.finished())
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), list('▢ e ▢ a ▢ ▢ t'.split(' ')))
        self.assertFalse(self.g1.finished())
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), list('▢ e ▢ a u ▢ t'.split(' ')))
        self.assertFalse(self.g1.finished())
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), list('▢ e ▢ a u l t'.split(' ')))
        self.assertFalse(self.g1.finished())
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), list('d e ▢ a u l t'.split(' ')))
        self.assertFalse(self.g1.finished())
        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), list('d e f a u l t'.split(' ')))
        self.assertTrue(self.g1.finished())

    def testDisplayGuessed(self):
        self.g1.guess('e')
        self.assertEqual(self.g1.displayGuessed(), [('e', 1)])
        self.g1.guess('d')
        self.assertEqual(self.g1.displayGuessed(), [('e', 1), ('d', 0)])
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), [('e', 1), ('d', 0), ('a', 3)])
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), [('e', 1), ('d', 0), ('a', 3), ('t', 6)])
        self.g1.guess('l')
        self.assertEqual(self.g1.displayGuessed(), [('e', 1), ('d', 0), ('a', 3), ('t', 6), ('l', 5)])
        self.g1.guess('f')
        self.assertEqual(self.g1.displayGuessed(), [('e', 1), ('d', 0), ('a', 3), ('t', 6), ('l', 5), ('f', 2)])
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), [('e', 1), ('d', 0), ('a', 3), ('t', 6), ('l', 5), ('f', 2), ('u', 4)])
