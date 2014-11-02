from exceptions.exceptions import InvalidRotorInputException

class Rotor:

    __substitution_cipher = []

    def __init__(self, substitution_order):
        self.__substitution_cipher = list(substitution_order)

    def get_substitution_character_for_given_input(self, input_character):
        index_of_character = ord(input_character) - 65
        if(index_of_character < 0 or index_of_character > 25):
            raise(InvalidRotorInputException)
        return self.__substitution_cipher[index_of_character]
