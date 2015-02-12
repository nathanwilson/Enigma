from rotor import Rotor

from exceptions.exceptions import NoRotorsInHouseException

class RotorHouse:
   
    __rotor = None

    def add_rotor(self, rotor_substitution_order): 
        self.__rotor = Rotor(rotor_substitution_order)

    def process_letter(self, input_character):
        if self.__rotor is None:
            raise(NoRotorsInHouseException)
        else:
            return self.__rotor.get_substitution_character_for_given_input(input_character)
