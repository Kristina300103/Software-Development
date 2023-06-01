import math
import sys
import unittest


def main(*args):
    try:
        x = float(args[0][1])
        if x <= 0.8:
            return math.sin(x) ** 2 - math.sqrt(x ** 3)
        else:
            return x ** 2 * math.cos(x) + 2 * x
    except:
        return "Произошла ошибка"

class SolverOfASystemOfEquationsTestCase(unittest.TestCase):
    def test_le(self):
        res = main(['...', 0.5])
        self.assertEqual(res, -0.12370454352734364)

    def test_r(self):
        res = main(['...', 0.9])
        self.assertEqual(res, 2.303504074299238)

    def test_error(self):
        res = main()
        self.assertEqual(res, "Произошла ошибка")