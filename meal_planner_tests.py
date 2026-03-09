#!/opt/homebrew/bin/python3
import unittest
from MealPlanner import hello_world


class TestFunctionality(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello World")

    def test_one_equals_one(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()