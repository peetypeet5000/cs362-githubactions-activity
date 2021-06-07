import unittest
import calculator


class TestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.add(1, 1), 2)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(calculator.sub(1, 1), 0)
        self.assertEqual(calculator.sub(5, -5), 10)
        self.assertEqual(calculator.sub(10.5, 5.5), 5)

    def test_multi(self):
        self.assertEqual(calculator.mult(1, 2), 2)
        self.assertEqual(calculator.mult(5, -5), -25)
        self.assertEqual(calculator.mult(.5, .5), .25)

    def test_div(self):
        self.assertEqual(calculator.div(2, 1), 2)
        self.assertEqual(calculator.div(25, 5), 5)
        self.assertEqual(calculator.div(-100, 10), -10)


# enables running directly
if __name__ == "__main__":
    unittest.main(verbosity=2)
