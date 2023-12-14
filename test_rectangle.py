import unittest
from rectangle import area
from rectangle import perimeter

class RectangleTestCase(unittest.TestCase):

    def test_rectangle_area_correct(self):
        self.assertEqual(area(2, 3), 2 * 3)

    def test_rectangle_area_wrong(self):
        self.assertRaises(Exception, area, -2, 2)

    def test_rectangle_area_null(self):
        self.assertEqual(area(0, 0), 0)

    def test_rectangle_perimeter_correct(self):
        self.assertEqual(perimeter(2, 3), (2 + 3) * 2)

    def test_rectangle_perimeter_wrong(self):
        self.assertRaises(Exception, area, -2, 2)

    def test_rectangle_perimeter_symbol(self):
        self.assertRaises(Exception, area, 'one', 2)
        
if __name__ == '__main__':
    unittest.main()
