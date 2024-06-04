import unittest
from unittest import TestCase

from step1 import printpole, autofill, pole1, pole2, place_ship, init_field


class MyTestCase(unittest.TestCase):
    def test_autofill(self):
        init_field(pole1)
        init_field(pole2)
        autofill(pole1)
        printpole(pole1, pole2)
        total = 0
        for yy in range(10):
            for xx in range(10):
                if (pole1[yy])[xx] > 0:
                    total += 1
        self.assertEqual(4 + 3 * 2 + 2 * 3 + 4, total)

    def test_place_ship(self):
        init_field(pole1)
        init_field(pole2)
        self.assertTrue(place_ship(pole1, 3, 1, 0, 0))
        self.assertFalse(place_ship(pole1, 3, 1, 0, 0))
        printpole(pole1, pole2)


if __name__ == '__main__':
    unittest.main()
