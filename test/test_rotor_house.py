import unittest

from src.rotor_house import RotorHouse
from src.exceptions.exceptions import NoRotorsInHouseException
from src.exceptions.exceptions import NoReflectorInHouseException

class TestRotorHouse(unittest.TestCase):
    def setUp(self):
        self.rotor_house = RotorHouse()

    def test_house_with_no_rotors(self):
        input_character = 'A'
        with self.assertRaises(NoRotorsInHouseException):
            self.rotor_house.process_letter(input_character)

    def test_house_with_no_reflector(self):
        input_character = 'A'
        self.rotor_house.add_rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        with self.assertRaises(NoReflectorInHouseException):
            self.rotor_house.process_letter(input_character)

    def test_get_char_forward_rotor_journey_single_rotor(self):
        self.rotor_house.add_rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        input_char = 'D'
        expected_output = 'F'
        actual_output = self.rotor_house.get_char_forward_rotor_journey(input_char)
        self.assertEqual(actual_output, expected_output)

    def test_get_char_forward_rotor_journey_multiple_rotors(self):
        self.rotor_house.add_rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        self.rotor_house.add_rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE')
        self.rotor_house.add_rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO')
        input_char = 'D'
        expected_output = 'R'
        actual_output = self.rotor_house.get_char_forward_rotor_journey(input_char)
        self.assertEqual(actual_output, expected_output)

    def test_get_char_return_rotor_journey_single_rotor(self):
        self.rotor_house.add_rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        input_char = 'F'
        expected_output = 'D'
        actual_output = self.rotor_house.get_char_return_rotor_journey(input_char)
        self.assertEqual(actual_output, expected_output)

    def test_get_char_return_rotor_journey_multiple_rotors(self):
        self.rotor_house.add_rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        self.rotor_house.add_rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE')
        self.rotor_house.add_rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO')
        input_char = 'R'
        expected_output = 'D'
        actual_output = self.rotor_house.get_char_return_rotor_journey(input_char)
        self.assertEqual(actual_output, expected_output)

    def test_get_char_reflect(self):
        self.rotor_house.add_reflector('EJMZALYXVBWFCRQUONTSPIKHGD')
        input_char = 'Z'
        expected_output = 'D'
        actual_output = self.rotor_house.get_char_reflect(input_char)
        self.assertEqual(actual_output, expected_output)

    def test_process_letter_with_single_rotor_character(self):
        self.rotor_house.add_rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        self.rotor_house.add_reflector('EJMZALYXVBWFCRQUONTSPIKHGD')

        input_char = 'E'
        expected_output = 'D'
        actual_output = self.rotor_house.process_letter(input_char)
        self.assertEqual(actual_output, expected_output)

    def test_process_letter_with_multiple_rotors_character(self):
        self.rotor_house.add_rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        self.rotor_house.add_rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE')
        self.rotor_house.add_rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO')
        self.rotor_house.add_reflector('EJMZALYXVBWFCRQUONTSPIKHGD')

        input_char = 'E'
        expected_output = 'C'
        actual_output = self.rotor_house.process_letter(input_char)
        self.assertEqual(actual_output, expected_output)

    def test_house_with_three_rotors_complete_rotation(self):
        self.rotor_house.add_rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        self.rotor_house.add_rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE')
        self.rotor_house.add_rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO')

        self.rotor_house.add_reflector('EJMZALYXVBWFCRQUONTSPIKHGD')

        for x in range(0, 26*26*26):
            self.rotor_house.process_string('H')

        self.assertEqual(self.rotor_house.get_rotors()[0].get_number_of_rotations(), 26*26, "Rotor 0 failure")
        self.assertEqual(self.rotor_house.get_rotors()[1].get_number_of_rotations(), 26, "Rotor 1 failure")
        self.assertEqual(self.rotor_house.get_rotors()[2].get_number_of_rotations(), 1, "Rotor 2 failure")


    def test_encrypt_decrypt_string(self):
        self.rotor_house.add_rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        self.rotor_house.add_rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE')
        self.rotor_house.add_rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO')

        self.rotor_house.add_reflector('EJMZALYXVBWFCRQUONTSPIKHGD')

        plaintext = "HELLOTHISISNATHAN"
        ciphertext = self.rotor_house.process_string(plaintext)

        another_rotor_house = RotorHouse()
        another_rotor_house.add_rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        another_rotor_house.add_rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE')
        another_rotor_house.add_rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO')

        another_rotor_house.add_reflector('EJMZALYXVBWFCRQUONTSPIKHGD')

        expected_plaintext = another_rotor_house.process_string(ciphertext)

        self.assertEqual(expected_plaintext, plaintext)
