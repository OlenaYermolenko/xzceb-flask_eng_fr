import unittest
from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(None), 'Provide some text for translation') # test when parameter is null
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when input is Hello and output Bonjour
        self.assertNotEqual(english_to_french('Hi'), 'Hola')  # test when input is Hi and output Hola

class Testfrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(None), 'Fournir un texte pour la traduction') # test when parameter is null
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  # test when input is Bonjour and output Hello
        self.assertNotEqual(french_to_english('Salut'), 'Hola')  # test when input is Salut and output Hola

unittest.main()
