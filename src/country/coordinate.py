# -*- coding: utf-8 -*-
class Coordinate:
    """Represent a ?."""

    def __init__(self, longitude, latitude, city):
        self.longitude = longitude
        self.latitude = latitude
        self.city = city

    def __str__(self):
        return "({}, {})".format(self.longitude, self.latitude)

    def get_city(self):
        return self.city

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash((self.longitude, self.latitude))