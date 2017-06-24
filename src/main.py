from src.exceptions.exceptions import *

from rotor_house import RotorHouse
from plugboard import Plugboard

import sys

if len(sys.argv) < 2:
    print 'Must provide text to encrypt'
    exit(1)

input_string = str(sys.argv[1])

if not input_string.isupper():
    print 'Input must be all upper case'
    exit(1)

if not input_string.isalpha():
    print 'Input must only contain letters'
    exit(1)

plugboard = Plugboard('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

rotor_house = RotorHouse()
rotor_house.add_rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q')
rotor_house.add_rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E')
rotor_house.add_rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'M')
rotor_house.add_reflector('EJMZALYXVBWFCRQUONTSPIKHGD')


print input_string

print plugboard.process_string(rotor_house.process_string(plugboard.process_string(input_string)))
