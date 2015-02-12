import unittest

from src.rotor import Rotor
from src.exceptions.exceptions import InvalidRotorInputException

class TestRotor(unittest.TestCase):
    def setUp(self):
        self.rotor = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')

    def test_single_input_is_mapped_to_correct_output(self):
       input_character = 'A'
       expected_output_character = 'E'
       self.assertEqual(self.rotor
                        .get_substitution_character_for_given_input(
                            input_character), expected_output_character, 
                        "Expected the output to be 'E' when given input 'A'")

    def test_rotor_rotates(self):
        start_rotation_status = self.rotor.get_current_rotation_status()
        self.rotor.rotate()
        second_rotation_status = self.rotor.get_current_rotation_status()
        expected_second_rotation_status = list('KMFLGDQVZNTOWYHXUSPAIBRCJE')
        self.assertEqual(second_rotation_status, expected_second_rotation_status,
                            "Actual output did not match expected output. Actual was: ".join(second_rotation_status))

    def test_exception_is_thrown_when_invalid_substitution_input_is_used(self):
        input_character = 'a'
        with self.assertRaises(InvalidRotorInputException):
            self.rotor.get_substitution_character_for_given_input(input_character)

if __name__ == '__main__':
    unittest.main()
