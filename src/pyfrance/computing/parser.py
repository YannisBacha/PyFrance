import codecs
import csv

from pyfrance.city import City


class Parser:
    """Parse a csv file containing cities with coordinates"""
    def __init__(self, filename, min_pop=None):
        """Create a new parser
        
        :param filename: the name of the csv file
        :param min_pop: the minimum population to compute the city
        """
        self.filename = filename
        self.cities = {}
        self.min_pop = min_pop

    def parse(self):
        """Parse the file and fill the cities set"""
        with codecs.open(self.filename, 'r', encoding='utf-8', errors='ignore') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if row[1] == 'nom':
                    continue
                c = City(row[0], row[1], int(row[2]), float(row[4].replace(',', '.')), float(row[3].replace(',', '.')))
                if self.min_pop is None or self.min_pop < c.population:
                    self.cities[c.id] = c
        print("{0} cities created".format(len(self.cities)))
