from math import radians, cos, sin, asin, sqrt


class Builder:
    """Build the graph with cities"""

    def __init__(self, cities, max_dist=None):
        """Create a new builder
        
        :param cities: a set containing City objects
        :param max_dist: the maximum distance to create a link between two cities
        """
        self.cities = cities
        self.max_dist = max_dist

    def build(self):
        """Build the graph by filling cities' neighbors"""
        links = 0
        for key1 in self.cities:
            city = self.cities[key1]
            for key2 in self.cities:
                other = self.cities[key2]
                if city != other:
                    dist = Builder.haversine(city.coordinates.latitude,
                                             city.coordinates.longitude,
                                             other.coordinates.latitude,
                                             other.coordinates.longitude)
                    if self.max_dist is None or self.max_dist > dist:
                        city.add_neighbor(other, dist)
                        links += 1
        print("{0} links created".format(links))

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

