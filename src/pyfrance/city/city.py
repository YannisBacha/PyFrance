# -*- coding: utf-8 -*-
from src.country import Country


class City:
    """Represent a city."""

    def __init__(self, id, name, population, longitude, latitude, country):
        """Build a new city

        :param id: the id of the city
        :param name: the name of the city
        :param population: the number of people who live in the city
        :param longitude: the longitude of the city
        :param latitude: the longitude of the city
        """
        self.id = id
        self.name = name
        self.population = population
        self.longitude = longitude
        self.latitude = latitude
        self.country = country

    def add_to_country(self, country):
        self.country.set_city(self.longitude, self.latitude, self)

    def __str__(self):
        return "{0} {1} {2} {3} {4}".format(self.id, self.name, self.population, self.longitude, self.latitude)

    def __repr__(self):
        return str(self)
