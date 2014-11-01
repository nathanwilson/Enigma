import unittest

from Engima import Rotor

class TestRotor(unittest.TestCase):
    def setUp(self):
        self.rotor = Rotor()

    def test_rotor_is_created(self):
            self.assertEqual(1, 2)


if __name__ == '__main__':
    unittest.main()
