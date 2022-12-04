""" Module for unit testing translator.py """
import unittest

from translator import englishToFrench, frenchToEnglish


class TestFrenchToEnglish(unittest.TestCase):
    """
        Class with unit test for translator.frenchToEnglish
    """
    def test_frenchToEnglish_assertEqual(self):
        """
            Test for the translation of the word ‘Bonjour’ and ‘Hello’.
        """
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

    def test_frenchToEnglish_assertEqual_None(self):
        """
            # Test for null input for frenchToEnglish
        """                
        self.assertEqual(frenchToEnglish(None), None)

    def test_frenchToEnglish_assertNotEqual(self):
        """
            # Test for the translation of the world ‘Bonjour’ and ‘Good bye’.
        """        
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Good bye')


class TestEnglishToFrench(unittest.TestCase):
    """
        Class with unit test for translator.englishToFrench
    """
    def test_englishToFrench_assertEqual(self):
        """
            # Test for the translation of the world ‘Hello’ and ‘Bonjour’
        """        
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def test_englishToFrench_assertEqual_None(self):
        """
            # Test for null input for englishToFrench
        """        
        self.assertEqual(englishToFrench(None), None)

    def test_englishToFrench_assertNotEqual(self):
        """
            # Test for the translation of the world ‘Hello’ and ‘Au revoir’.
        """        
        self.assertNotEqual(frenchToEnglish('Hello'), 'Au revoir')


unittest.main()
