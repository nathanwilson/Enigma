import unittest

from src.rotor_house import RotorHouse
from src.exceptions.exceptions import NoRotorsInHouseException

class TestRotorHouse(unittest.TestCase):
    def setUp(self):
        self.rotor_house = RotorHouse()

    def test_rotor_house_is_created(self):
        self.assertIsNotNone(self.rotor_house)
    
    def test_house_with_one_rotor_maps_given_input_to_expected_output(self):
        input_character = 'A'
        expected_output_character = 'E'
        self.rotor_house.add_rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        self.assertEqual(self.rotor_house.process_letter(input_character),
                expected_output_character,
                "Expected the output to be 'E' when given input 'A'")


    def test_house_with_no_rotors(self):
        input_character = 'A'
        with self.assertRaises(NoRotorsInHouseException):
            self.rotor_house.process_letter(input_character)
