import unittest
from circle import area
from circle import perimeter

class TestCircle(unittest.TestCase):
    
    def test_circle_area_correct(self):
        res = area(3)
        self.assertAlmostEqual(res, 28.274, delta=0.01)
        
    def test_circle_area_wrong(self):
        self.assertRaises(Exception, area, -2)
        self.assertRaises(Exception, area, -1)

    def test_circle_area_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_circle_perimeter_correct(self):
        res = area(3)
        self.assertAlmostEqual(res, 18.849, delta=0.01)

    def test_circle_perimeter_wrong(self):
        self.assertRaises(ValueError, perimeter, -2)
        self.assertRaises(ValueError, perimeter, -1)
        
    def test_circle_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)
        
if __name__ == '__main__':
    unittest.main()
