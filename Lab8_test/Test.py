import unittest
from Lab8.main import prim_mst


class TestPrimAlgorithm(unittest.TestCase):
    def test_small_graph(self):
        matrix = [
            [0, 2, 3],
            [2, 0, 1],
            [3, 1, 0]
        ]
        total_length, _ = prim_mst(matrix)
        self.assertEqual(total_length, 3)


    def test_medium_graph(self):
        matrix = [
            [0, 2, 3, 0, 0],
            [2, 0, 1, 4, 0],
            [3, 1, 0, 5, 0],
            [0, 4, 5, 0, 7],
            [0, 0, 0, 7, 0]
        ]
        total_length, _ = prim_mst(matrix)
        self.assertEqual(total_length, 14)


    def test_disconnected_graph(self):
        matrix = [
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 0]
        ]
        result = prim_mst(matrix)
        self.assertEqual(result, (None, None))


    def test_single_node(self):
        matrix = [[0]]
        total_length, _ = prim_mst(matrix)
        self.assertEqual(total_length, 0)


if __name__ == '__main__':
    unittest.main()
