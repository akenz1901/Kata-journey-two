import unittest
from kata import vowel_detector


class VowelDetectorTest(unittest.TestCase):

    def test_for_vowel_extraction(self):
        alphabeth = "honorable"
        self.assertEqual(vowel_detector.confirm_vowels(alphabeth), ['h', 'n', 'r', 'b', 'l'])
        self.assertEqual(vowel_detector.remove_vowel(alphabeth), 'hnrbl')