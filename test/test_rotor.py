import unittest

from src.rotor import Rotor
from src.exceptions.invalid_rotor_input_exception import InvalidRotorInputException

class TestRotor(unittest.TestCase):
    def setUp(self):
        self.rotor = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')

    def test_rotor_is_created(self):
        self.assertIsNotNone(self.rotor)

    def test_input_substituion_sequence_is_properly_set(self):
       input_character = 'A'
       expected_output_character = 'E'
       self.assertEqual(self.rotor
                        .get_substitution_character_for_given_input(
                            input_character), expected_output_character, 
                        "Expected the output to be 'E' when given input 'A'")


    def test_exception_is_thrown_when_invalid_substitution_input_is_used(self):
        input_character = 'a'
        with self.assertRaises(InvalidRotorInputException):
            self.rotor.get_substitution_character_for_given_input(input_character)

if __name__ == '__main__':
    unittest.main()
