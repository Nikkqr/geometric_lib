import unittest
from square import area
from square import perimeter

class TestSquare(unittest.TestCase):
    
    def test_square_area_correct(self):
        self.assertEqual(area(2), 2 * 2)

    def test_square_area_wrong(self):
        self.assertRaises(Exception, area, -2)

    def test_square_area_null(self):
        self.assertEqual(area(0), 0)

    def test_square_perimeter_correct(self):
        self.assertEqual(perimeter(2), 4 * 2)

    def test_square_perimter_wrong(self):
        self.assertRaises(Exception, perimeter, -2)

    def test_square_perimeter_null(self):
          self.assertEqual(perimeter(0), 0)
        
if __name__ == '__main__':
    unittest.main()
