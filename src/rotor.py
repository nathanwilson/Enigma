from exceptions.exceptions import InvalidRotorInputException

class Rotor:

    __substitution_cipher = []
    __full_rotations = 0
    __rotation_value = 0
    __CONVERT_FROM_ASCII = 65
    __MIN_INDEX_OF_CIPHER = 0
    __MAX_INDEX_OF_CIPHER = 25

    def __init__(self, substitution_order):
        self.__substitution_cipher = list(substitution_order)
        self.__full_rotations = 0
        self.__rotation_value = 0

    def get_substitution_character_for_given_input(self, input_character):
        index_of_character = ord(input_character) - self.__CONVERT_FROM_ASCII
        if(index_of_character < self.__MIN_INDEX_OF_CIPHER
                or index_of_character > self.__MAX_INDEX_OF_CIPHER):
            raise(InvalidRotorInputException)
        return self.__substitution_cipher[index_of_character]

    def get_reverse_substitution_character_for_given_input(self, input_character):
        temp = 'A'
        for char in self.__substitution_cipher:
            if char == input_character:
                return temp
            temp = chr(ord(temp) + 1)

    def rotate(self):
        temp = self.__substitution_cipher[0]
        for x in range(0, len(self.__substitution_cipher) - 1):
            self.__substitution_cipher[x] = self.__substitution_cipher[x + 1]
        self.__substitution_cipher[25] = temp
        self.__rotation_value = (self.__rotation_value + 1) % 26
        if(self.__rotation_value is 0):
            self.__full_rotations = self.__full_rotations + 1

    def get_number_of_rotations(self):
        return self.__full_rotations

    def get_current_rotation_value(self):
        return self.__rotation_value

    def get_current_rotation_status(self):
        return self.__substitution_cipher
