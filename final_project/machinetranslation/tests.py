"""importing unittest"""
import unittest
from translator import englishToFrench, frenchToEnglish


class TestTranslation(unittest.TestCase):
    """test case is here"""
    def english_to_french(self):
        """e2f test function"""
        self.assertEqual(englishToFrench("Hello"),"Bonjur")
        # test when "Hello" given as input the output is "Bonjur"
        self.assertNotEqual(englishToFrench("Hello"),"Hello")
        # test when "Hello" given as input the output is not "Hello"

    def french_to_english(self):
        """f2e test function"""
        self.assertEqual(frenchToEnglish("Bonjur"),"Hello")
        # test when "Bonjur" given as input the output is "Hello"
        self.assertNotEqual(frenchToEnglish("Bonjur"),"Bonjur")
        # test when "Bonjur" given as input the output is not "Bonjur"
