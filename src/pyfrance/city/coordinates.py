class Coordinates:
    """Represent gps coordinates"""

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return "<lat:{0}, lon:{1}>".format(self.latitude, self.longitude)

    def __repr__(self):
        return str(self)
