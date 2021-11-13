#!python

class Coordinate:
    """Coordinate on Earth."""

    reference_system = "WGS84"

    def __init__(self, lat=0.0, lon=0.0):
        self.lat = lat
        self.lon = lon
    
    def __repr__(self):
        return f'Coordinate({self.lat}, {self.lon})'
   
    def __str__(self):
        ns = "NS"[self.lat < 0]
        ew = "EW"[self.lon < 0]
        return f'{abs(self.lat):.1f} deg {ns}, {abs(self.long):.1f} deg {ew}'

    def geohash(self):
        from geohash import encode
        return encode(self.lat, self.lon)

