import unittest

from src.rotor_house import RotorHouse
from src.exceptions.exceptions import NoRotorsInHouseException

class TestRotorHouse(unittest.TestCase):
    def setUp(self):
        self.rotor_house = RotorHouse()
    
    def test_house_with_one_rotor_maps_given_input_to_expected_output(self):
        input_character = 'A'
        expected_output_character = 'E'
        self.rotor_house.add_rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        actual_output_character = self.rotor_house.process_letter(input_character)
        self.assertEqual(actual_output_character,
                expected_output_character,
                "Expected the output to be 'E' when given input 'A'")

    def test_house_with_two_rotors_maps_given_input_to_expected_output(self):
        input_character = 'A'
        expected_output_character = 'S'
        self.rotor_house.add_rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        self.rotor_house.add_rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE')
        actual_output_character = self.rotor_house.process_letter(input_character)
        self.assertEqual(actual_output_character,
                expected_output_character,
                "Expected the output to be 'S' when given input 'A'")

    def test_house_with_two_rotors_maps_given_inputs_to_expect_outputs(self):
        input_character_one = 'A'
        input_character_two = 'M'
        expected_output_character_one = 'S'
        expected_output_character_two = 'F'
        self.rotor_house.add_rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        self.rotor_house.add_rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE')
        actual_output_character_one = self.rotor_house.process_letter(input_character_one)
        actual_output_character_two = self.rotor_house.process_letter(input_character_two)
        self.assertEqual(actual_output_character_one,
                expected_output_character_one,
                "Expected the first output to be 'S' when given inputs 'AM'")
        self.assertEqual(actual_output_character_two,
                expected_output_character_two,
                "Expected the second output to be 'F' when given inputs 'AM'")

    def test_house_with_two_rotors_maps_given_input_string_to_expected_output(self):
        input_string = 'HELLO'
        expected_output_string = 'QRFOZ'
        self.rotor_house.add_rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        self.rotor_house.add_rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE')
        actual_output_string = self.rotor_house.process_string(input_string)
        self.assertEqual(actual_output_string,
                expected_output_string,
                "Expected the output to be 'QRFOZ' when given input 'HELLO'")

    def test_house_with_three_rotors_maps_input_string_to_expected_output(self):
        input_string = 'HELLO'
        expected_output_string = 'IWLYO'
        self.rotor_house.add_rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        self.rotor_house.add_rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE')
        self.rotor_house.add_rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO')
        actual_output_string = self.rotor_house.process_string(input_string)
        self.assertEqual(actual_output_string,
                expected_output_string,
                "Expected the output to be 'IWLYO' when given input 'HELLO'")

    def test_house_with_no_rotors(self):
        input_character = 'A'
        with self.assertRaises(NoRotorsInHouseException):
            self.rotor_house.process_letter(input_character)
