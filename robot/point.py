class Point(object):
    """"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Add input point to current point."""
        return Point(self.x + other.x, self.y + other.y)

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y
