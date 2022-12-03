""" Module for unit testing translator.py """
import unittest

from translator import englishToFrench, frenchToEnglish


class TestFrenchToEnglish(unittest.TestCase):
    """
        Class with unit test for translator.frenchToEnglish
    """
    def test1(self):
        """
            First unit test
        """
        # Test for null input for frenchToEnglish
        self.assertEqual(frenchToEnglish(None), None)

        # Test for the translation of the world ‘Bonjour’ and ‘Hello’.
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

class TestEnglishToFrench(unittest.TestCase):
    """
        Class with unit test for translator.englishToFrench
    """
    def test1(self):
        """
            First unit test
        """
        # Test for null input for englishToFrench
        self.assertEqual(englishToFrench(None), None)

        # Test for the translation of the world ‘Hello’ and ‘Bonjour’
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

unittest.main()
