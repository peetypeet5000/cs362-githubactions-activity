import unittest
import calculator


class TestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.add(1, 1), 2)
        self.assertEqual(calculator.add(-1, 1), 0)


# enables running directly
if __name__ == "__main__":
    unittest.main(verbosity=2)
