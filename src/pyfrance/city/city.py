from .coordinates import Coordinates


class City:
    """Represent a city."""

    def __init__(self, id, name, population, latitude, longitude):
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
        self.coordinates = Coordinates(latitude, longitude)
        self.neighbors = set()

    def add_neighbor(self, city):
        self.neighbors.add(city)

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.id, self.name, self.population, self.coordinates)

    def __repr__(self):
        return str(self)
