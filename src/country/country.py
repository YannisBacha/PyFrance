# -*- coding: utf-8 -*-
from src.country.coordinate import Coordinate


class Country:
    """Represent a city."""

    def __init__(self, name):
        """Build a new country

        :param name: the name of the country
        """
        self.name = name
        self.coordinates = {}

    def set_city(self, longitude, latitude, city):
        """Set the city at its longitude / latitude

        :param longitude: the longitude of the city
        :param latitude: the latitude of the city
        :param city: the city
        :raise ValueError: the coordinates must be valid
        """
        self.coordinates[Coordinate(longitude, latitude, city)] = city

    def get_distance_between_cities(self, city):
        distances = set()
        for c in self.coordinates:
            if(c != city):
                longitude = abs(self.string_to_num(city.longitude) - self.string_to_num(c.longitude))
                latitude = abs(self.string_to_num(city.latitude) - self.string_to_num(c.latitude))
                distances.add(Coordinate(longitude, latitude,c))
        return distances

    def get_city_by_name(self, name):
        for c in self.coordinates:
            city = c.get_city()
            if(city.name == name):
                return city
        return None

    def __str__(self):
        return "{0}".format(self.name)

    def string_to_num(self, s):
        try:
            return int(s)
        except ValueError:
            return float(s.replace(',', '.'))
