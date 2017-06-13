#! /usr/bin/python3.6
import random
import time

from pyfrance.computing import *


p = Parser('../resources/CommunesFrance.csv', 10000)
t1 = time.time()
p.parse()
t2 = time.time()
print("{0}ms".format((t2 - t1) * 1000))
b = Builder(p.cities, 50)
t1 = time.time()
b.build()
t2 = time.time()
print("{0}s".format((t2 - t1)))
c = p.cities[random.sample(list(p.cities), 1)[0]]
print(c.name, len(c.neighbors), "neighbors", c.neighbors)
