import unittest
from circle import area
from circle import perimeter

class TestCircle(unittest.TestCase):
    
    def test_circle_area_correct(self):
        self.assertEqual(area(3), math.pi * 3 * 3)
        
    def test_circle_area_wrong(self):
        self.assertRaises(Exception, area, -2)
        self.assertRaises(Exception, area, -1)

    def test_circle_area_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_circle_perimeter_correct(self):
        self.assertEqual(perimeter(3), 2 * math.pi * 3)

    def test_circle_perimeter_wrong(self):
        self.assertRaises(ValueError, perimeter, -2)
        self.assertRaises(ValueError, perimeter, -1)
        
    def test_circle_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)
        
if __name__ == '__main__':
    unittest.main()
