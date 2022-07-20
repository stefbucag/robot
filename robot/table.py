class Table(object):
    """Limited area/dimension where the robot is allowed to move."""

    def __init__(self, llc, urc):
        self.llc = llc
        self.urc = urc

    def bounds(self, point):
        """Checks if the robot is within the square table boundary/dimensions."""
        return self.llc <= point and self.urc >= point
