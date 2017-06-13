from math import radians, cos, sin, asin, sqrt


class Builder:
    """Build the graph with cities"""

    def __init__(self, cities):
        """Create a new builder
        
        :param cities: a set containing City objects
        """
        self.cities = cities

    def build(self):
        for city in self.cities:
            for other in self.cities:
                print("{0} {1} {2}".format(city.name,
                                           Builder.haversine(city.coordinates.latitude,
                                                             city.coordinates.longitude,
                                                             other.coordinates.latitude,
                                                             other.coordinates.longitude),
                                           other.name))

    @staticmethod
    def haversine(lat1, lon1, lat2, lon2):
        """Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees)
        """
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371
        return c * r

