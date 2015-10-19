from rotor import Rotor

from src.exceptions.exceptions import NoRotorsInHouseException
from src.exceptions.exceptions import NoReflectorInHouseException

class RotorHouse:

    __rotor = []
    __reflector = None

    def __init__(self):
        self.__rotor = []

    def add_rotor(self, substitution_order, rotation_char):
        self.__rotor.append(Rotor(substitution_order, rotation_char))

    def add_reflector(self, substitution_order):
        self.__reflector = Rotor(substitution_order, None)

    def check_house_has_rotors(self):
        if not self.__rotor:
            raise(NoRotorsInHouseException)

    def check_house_has_reflector(self):
        if self.__reflector is None:
            raise(NoReflectorInHouseException)

    def get_char_forward_rotor_journey(self, input_character):
        current_character = input_character
        for rotor in self.__rotor:
            current_character = rotor.get_substitution_character_for_given_input(current_character)
        return current_character

    def get_char_return_rotor_journey(self, input_character):
        current_character = input_character
        for rotor in reversed(self.__rotor):
            current_character = rotor.get_reverse_substitution_character_for_given_input(current_character)
        return current_character

    def get_char_reflect(self, input_character):
        return self.__reflector.get_substitution_character_for_given_input(input_character)

    def perform_first_rotor_rotate(self, rotor):
        rotor.rotate()

    def perform_non_first_rotor_rotate(self, rotor, previous_rotor):
        if previous_rotor.get_turnover_status() is True:
            rotor.rotate()

    def perform_rotate(self):
        previous_rotor = None
        for rotor in self.__rotor:
            if previous_rotor is None:
                self.perform_first_rotor_rotate(rotor)
            else:
                self.perform_non_first_rotor_rotate(rotor, previous_rotor)
            previous_rotor = rotor

    def process_letter(self, input_character):
        self.check_house_has_rotors()
        self.check_house_has_reflector()

        current_character = input_character
        current_character = self.get_char_forward_rotor_journey(current_character)
        current_character = self.get_char_reflect(current_character)
        current_character = self.get_char_return_rotor_journey(current_character)
        self.perform_rotate()

        return current_character

    def process_string(self, input_string):
        self.check_house_has_rotors()
        output_string = ''
        for char in input_string:
            output_string = output_string + self.process_letter(char)
        return output_string

    def get_rotors(self):
        return self.__rotor
