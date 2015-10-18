import unittest

from src.rotor import Rotor
from src.exceptions.exceptions import InvalidRotorInputException

class TestRotor(unittest.TestCase):
    def setUp(self):
        self.rotor = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q')

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

    def test_full_rotation(self):
        for x in range(0, 26):
            self.rotor.rotate()
        self.assertEqual(self.rotor.get_number_of_rotations(), 1, "Should have completed a full rotation")


    def test_reverse_substitution_first_letter(self):
        input_character = 'E'
        expected_output_character = 'A'
        actual = self.rotor.get_reverse_substitution_character_for_given_input(input_character)
        self.assertEqual(actual, expected_output_character,
                            "Expected the output to be 'A' when given 'E' but got " + actual)

    def test_reverse_substitution_last_letter(self):
        input_character = 'J'
        expected_output_character = 'Z'
        actual = self.rotor.get_reverse_substitution_character_for_given_input(input_character)
        self.assertEqual(actual, expected_output_character,
                            "Expected the output to be 'Z' when given 'J' but got " + actual)

    def test_rotate_reverse_substitution(self):
        input_character = 'K'
        expected_output_character = 'A'
        self.rotor.rotate()
        actual = self.rotor.get_reverse_substitution_character_for_given_input(input_character)
        self.assertEqual(actual, expected_output_character,
                            "Expected the output to be 'A' when given 'K' but got " + actual)

    def test_advance_next_rotor(self):
        for i in range(0, 7):
            self.assertEqual(self.rotor.get_turnover_status(), False)
            self.rotor.rotate()
        self.assertEqual(self.rotor.get_turnover_status(), True)



if __name__ == '__main__':
    unittest.main()
