from rotor import Rotor

from exceptions.exceptions import NoRotorsInHouseException

class RotorHouse:
   
    __rotor = []

    def __init__(self):
    	self.__rotor = []

    def add_rotor(self, rotor_substitution_order): 
        self.__rotor.append(Rotor(rotor_substitution_order))

    def check_house_has_rotors(self):
    	if not self.__rotor:
            raise(NoRotorsInHouseException)

    def process_letter(self, input_character):
    	self.check_house_has_rotors()
    	current_character = input_character
    	previous_rotor = None
    	for rotor in self.__rotor:
    		current_character = rotor.get_substitution_character_for_given_input(current_character)
    		if previous_rotor is None:
    			rotor.rotate()
    		elif previous_rotor.get_current_rotation_value() is 0:
    			rotor.rotate()
    		previous_rotor = rotor
    	return current_character

    def process_string(self, input_string):
    	self.check_house_has_rotors()
    	output_string = ''

    	for char in input_string:
    		output_string = output_string + self.process_letter(char)
    	return output_string
