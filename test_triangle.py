import unittest
from triangle import area
from triangle import perimeter

class TriangleTestCase(unittest.TestCase):

    def test_triangle_area_correct(self):
        self.assertEqual(area(4, 2), (4 * 2) / 2)

    def test_triangle_area_wrong(self):
        self.assertRaises(Exception, area, -2, 2)

    def test_triangle_area_null(self):
        self.assertEqual(area(0, 0), 0)

    def test_triangle_perimeter_correct(self):
        self.assertEqual(perimeter(1, 2, 3), 1 + 2 + 3)

    def test_triangle_perimeter_wrong(self):
        self.assertRaises(Exception, perimeter, -2, 2, -1)

    def test_triangle_perimeter_null(self):
        self.assertEqual(perimeter(0, 0, 0), 0)
        
if __name__ == '__main__':
    unittest.main()
