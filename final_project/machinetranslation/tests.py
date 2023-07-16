import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
	def test_eng_tofr(self):				# only functions with test_ are run so this name is important
		self.assertEqual(english_to_french("Hello"), "Pepitoooo")

	def test_frto_eng(self):
		self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == '__main__':
	unittest.main()