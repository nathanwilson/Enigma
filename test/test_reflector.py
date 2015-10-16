import unittest

from src.reflector import Reflector

class TestReflector(unittest.TestCase):
    def setUp(self):
        self.reflector = Reflector('EJMZALYXVBWFCRQUONTSPIKHGD')

    def test_single_input_is_mapped_to_correct_output(self):
       input_character = 'Z'
       expected_output_character = 'D'
       self.assertEqual(self.reflector
                        .get_substitution_character_for_given_input(
                            input_character), expected_output_character,
                            "Input characer 'Z' and expected 'D'. Did not get that.")


if __name__ == '__main__':
    unittest.main()
