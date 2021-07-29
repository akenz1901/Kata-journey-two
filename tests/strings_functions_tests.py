import unittest
from kata import strings_and_its_functions


class FindTest(unittest.TestCase):

    def test_for_find_method(self):
        word = "Hello_world"
        self.assertEqual(strings_and_its_functions.find(word, "o"), 4)

    def test_for_occurrence_of_a_character(self):
        word = "Hello_world"
        self.assertEqual(strings_and_its_functions.count_occurrence_of_character(word, "l"), 3)

    def test_split_function(self):
        sentence = "I will need to get to dubai tonight"
        self.assertEqual(strings_and_its_functions.split(sentence), ['I', 'will', 'need', 'to', 'get', 'to', 'dubai',
                                                                     'tonight'])

    def test_for_punctuation_removal(self):
        sentence = '"Well, I never did!", said Alice."'
        self.assertEqual(strings_and_its_functions.eliminate_punctuation(sentence), "Well I never did said Alice")
        sentence = "Are you very, very, sure?"
        self.assertEqual(strings_and_its_functions.eliminate_punctuation(sentence), 'Are you very very sure')

    def test_for_combination_of_split_and_punctuation(self):
        sentence = """Pythons are constrictors, which means that they will 'squeeze' the life
                           out of their prey. They coil themselves around their prey and with
                           each breath the creature takes the snake will squeeze a little tighter
                           until they stop breathing completely. Once the heart stops the prey
                           is swallowed whole. The entire animal is digested in the snake's
                           stomach except for fur or feathers. What do you think happens to the fur,
                           feathers, beaks, and eggshells? The 'extra stuff' gets passed out as ---
                           you guessed it --- snake POOP! """
        self.assertEqual(strings_and_its_functions.eliminate_punctuation(sentence).split(sentence))

    def test_string_format(self):
        self.assertEqual(strings_and_its_functions.display_string('michael', 4), "my name is michael i am 4 year old")

    def test_decimal_with_string_format(self):
        self.assertEqual(strings_and_its_functions.display_string_format_with_decimal("akenz", 21, ), "my name is akenz i am 21 year old i have %0.000000")