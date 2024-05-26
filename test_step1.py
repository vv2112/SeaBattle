import unittest

from step1 import printpole, autofill, pole1, pole2


class MyTestCase(unittest.TestCase):
    def test_autofill(self):
        autofill(pole1)
        printpole(pole1, pole2)
        total = 0
        for yy in range(10):
            for xx in range(10):
                if (pole1[yy])[xx] > 0:
                    total += 1
        self.assertEqual(4+3*2+2*3+4, total)

#        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
