"""
Модуль unit-тестов для rectangle.py

Запуск всех тестов:
    python -m unittest test_rectangle.py
Запуск с подробным выводом:
    python -m unittest test_rectangle.py -v
"""

import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):
    # Тесты для функции area()
    def test_area_normal_values(self):
        self.assertEqual(rectangle.area(5, 10), 50)
        self.assertEqual(rectangle.area(3, 7), 21)
    
    def test_area_zero(self):
        self.assertEqual(rectangle.area(0, 10), 0)
        self.assertEqual(rectangle.area(10, 0), 0)
        self.assertEqual(rectangle.area(0, 0), 0)
    
    def test_area_square(self):
        self.assertEqual(rectangle.area(5, 5), 25)
        self.assertEqual(rectangle.area(10, 10), 100)
    
    def test_area_float_values(self):
        self.assertAlmostEqual(rectangle.area(2.5, 4.0), 10.0)
        self.assertAlmostEqual(rectangle.area(3.14, 2), 6.28, places=2)
    
    def test_area_negative_values(self):
        with self.assertRaises(ValueError):
            rectangle.area(-5, 10)
        with self.assertRaises(ValueError):
            rectangle.area(5, -10)
        with self.assertRaises(ValueError):
            rectangle.area(-5, -10)
    
    def test_area_wrong_type(self):
        with self.assertRaises(TypeError):
            rectangle.area("10", 5)
        with self.assertRaises(TypeError):
            rectangle.area(10, [5])
    
    # Тесты для функции perimeter()
    def test_perimeter_normal_values(self):
        self.assertEqual(rectangle.perimeter(5, 10), 30)
        self.assertEqual(rectangle.perimeter(3, 7), 20)
    
    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(0, 10), 20)
        self.assertEqual(rectangle.perimeter(10, 0), 20)
        self.assertEqual(rectangle.perimeter(0, 0), 0)
    
    def test_perimeter_square(self):
        self.assertEqual(rectangle.perimeter(5, 5), 20)
        self.assertEqual(rectangle.perimeter(10, 10), 40)
    
    def test_perimeter_float_values(self):
        self.assertAlmostEqual(rectangle.perimeter(2.5, 4.0), 13.0)
        self.assertAlmostEqual(rectangle.perimeter(3.14, 2), 10.28, places=2)
    
    def test_perimeter_negative_values(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-5, 10)
        with self.assertRaises(ValueError):
            rectangle.perimeter(5, -10)
    
    def test_perimeter_wrong_type(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("10", 5)
        with self.assertRaises(TypeError):
            rectangle.perimeter(10, None)


if __name__ == "__main__":
    unittest.main(verbosity=2)