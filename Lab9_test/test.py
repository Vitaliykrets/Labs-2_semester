import unittest
from src.Lab9 import count_paths


class TestLab9(unittest.TestCase):
    def test_example1(self):
        grid = [
            "aaa",
            "cab",
            "def"
        ]
        self.assertEqual(count_paths(grid), 5)


    def test_example2(self):
        grid = ["abcdefaghi"]
        self.assertEqual(count_paths(grid), 2)


    def test_example3(self):
        grid = ["aaaaaaa"] * 6
        self.assertEqual(count_paths(grid), 201684)


    def test_single_cell(self):
        grid = ["z"]
        self.assertEqual(count_paths(grid), 1)


if __name__ == "__main__":
    unittest.main()
