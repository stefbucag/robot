from math import pi,sin,cos
from robot.point import Point

class Robot(object):
    """"""
    def __init__(self, location = Point(0.0, 0.0), facing = 0.0, table = None, directions = None):
        self.location = location
        self.facing = facing
        self.table = table
        self.directions = directions

    def left(self):
        """Rotate robot 90 degrees to the left"""
        return self.place(self.location, (self.facing - 0.5)%2, self.table)

    def right(self):
        """Rotate robot 90 degrees to the right"""
        return self.place(self.location, (self.facing + 0.5)%2, self.table)

    def move(self):
        """Move the robot to desired location within the table."""
        return self.place(self.location + Point(sin(pi * self.facing)
                                               ,cos(pi * self.facing))
                         ,self.facing, self.table)

    def report(self):
        """Report the robot's current location (X,Y and F)."""
        if self.table is not None:
            print(round(self.location.x), round(self.location.y), self.directions[round(self.facing*2)])
        return self

    def place(self, location, facing, table):
        """Responsible for the initial position of the robot."""
        if table is not None and table.bounds(location):
            return Robot(location, facing, table, self.directions)
