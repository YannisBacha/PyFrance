#! /usr/bin/python3.6
import random
import time

from pyfrance.computing import *
from pyfrance.pathfinding import *


def js_path(cities, path):
    for city_id in path:
        city = cities[city_id]
        print('{lat: ', city.coordinates.latitude, ', lng: ', city.coordinates.longitude, '},', sep='')

p = Parser('resources/CommunesFrance.csv', 10000)
t1 = time.time()
print("{0} cities created".format(p.parse()))
t2 = time.time()
print("{0}ms".format((t2 - t1) * 1000))

b = Builder(p.cities, 50)
t1 = time.time()
print("{0} links created".format(b.build()))
t2 = time.time()
print("{0}s".format((t2 - t1)))

dijkstra = Dijkstra(p.cities)
t1 = time.time()
path = dijkstra.compute_path('calais', 'marseille')
t2 = time.time()
print("{0}ms".format((t2 - t1) * 1000))
print(path)
t1 = time.time()
path = dijkstra.compute_path_priority_queue('calais', 'marseille')
t2 = time.time()
print("{0}ms".format((t2 - t1) * 1000))
print(path)

a_star = AStar(p.cities)
t1 = time.time()
path = a_star.compute_path('calais', 'marseille')
t2 = time.time()
print("{0}ms".format((t2 - t1) * 1000))
print(path)
t1 = time.time()
path = a_star.compute_path_priority_queue('calais', 'marseille')
t2 = time.time()
print("{0}ms".format((t2 - t1) * 1000))
print(path)

js_path(p.cities, path)
