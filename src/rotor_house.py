from rotor import Rotor

from exceptions.exceptions import NoRotorsInHouseException

class RotorHouse:
   
    __rotor = []

    def add_rotor(self, rotor_substitution_order): 
        self.__rotor.append(Rotor(rotor_substitution_order))
        print self.__rotor

    def process_letter(self, input_character):
        if not self.__rotor:
            raise(NoRotorsInHouseException)
        else:
            return self.__rotor[0].get_substitution_character_for_given_input(input_character)
