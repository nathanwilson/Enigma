import unittest

from src.rotor import Rotor

class TestRotor(unittest.TestCase):
    def setUp(self):
        self.rotor = Rotor()

    def test_rotor_is_created(self):
            self.assertIsNotNone(self.rotor)


if __name__ == '__main__':
    unittest.main()
