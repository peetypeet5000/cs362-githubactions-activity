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


# enables running directly
if __name__ == "__main__":
    unittest.main(verbosity=2)
