#! /usr/bin/python3.6
from pyfrance.computing import *


p = Parser('../resources/CommunesFrance.csv', 10000)
p.parse()
print(len(p.cities))
b = Builder(p.cities)
b.build()
