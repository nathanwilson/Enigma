import unittest

from src.plugboard import Plugboard
from src.exceptions.exceptions import InvalidRotorInputException

class TestPlugboard(unittest.TestCase):
    def setUp(self):
        self.plugboard = Plugboard('EKMFLGDQVZNTOWYHXUSPAIBRCJ')

    def test_single_input_is_mapped_to_correct_output(self):
       input_character = 'A'
       expected_output_character = 'E'
       self.assertEqual(self.plugboard
                        .get_substitution_character_for_given_input(
                            input_character), expected_output_character,
                        "Expected the output to be 'E' when given input 'A'")

if __name__ == '__main__':
    unittest.main()
