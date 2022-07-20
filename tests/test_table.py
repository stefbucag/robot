import unittest
from robot.table import Table
from robot.point import Point

class TestTable(unittest.TestCase):

    def test_bounds(self):
        point_A = Point(8,8)
        self.assertFalse(Table.bounds(point_A))

        point_B = Point(1,2)
        self.assertTrue(Table.bounds(point_B))


if __name__ == '__main__':
    unittest.main()
