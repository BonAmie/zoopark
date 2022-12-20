import unittest

from aviary import __init__

class Test_Call(unittest.TestCase):
    def setUp(self):
        self._calc=__init__

    def test_add(self, a, b, expeted):
        actual - self._calc.Add(a,b)
        self.assertEqual(expeted, actual)
    if __name__ == "__main__":
        unittest.main()
