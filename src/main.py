#! /usr/bin/python3.6
# -*- coding: utf-8 -*-
import csv
from src.city import City
from src.country import Country

cr = csv.reader(open("Test.csv","r"))
country = Country("France")
with open('CommunesFrance.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        if(row[1] == 'nom'):
            print("Nom    Population")
            continue
        c = City(row[0], row[1], row[2], row[3], row[4], country)
        c.add_to_country(country)
        #print(c)

    lyon = country.get_city_by_name("LYON")
    print(lyon)
    print(country.get_distance_between_cities(lyon))
