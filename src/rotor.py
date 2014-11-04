from exceptions.exceptions import InvalidRotorInputException

class Rotor:

    __substitution_cipher = []
    __CONVERT_FROM_ASCII = 65
    __MIN_INDEX_OF_CIPHER = 0
    __MAX_INDEX_OF_CIPHER = 25

    def __init__(self, substitution_order):
        self.__substitution_cipher = list(substitution_order)

    def get_substitution_character_for_given_input(self, input_character):
        index_of_character = ord(input_character) - self.__CONVERT_FROM_ASCII 
        if(index_of_character < self.__MIN_INDEX_OF_CIPHER
                or index_of_character > self.__MAX_INDEX_OF_CIPHER):
            raise(InvalidRotorInputException)
        return self.__substitution_cipher[index_of_character]
