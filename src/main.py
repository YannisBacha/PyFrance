#! /usr/bin/python3.6
# -*- coding: utf-8 -*-
import csv
from city.city import City

cr = csv.reader(open("Test.csv","r"))

with open('Test.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        if(row[1] == 'nom'):
            print("Id   Nom    Population")
            continue
        c = City(row[0], row[1], row[2], row[3], row[4])
        print(c)

