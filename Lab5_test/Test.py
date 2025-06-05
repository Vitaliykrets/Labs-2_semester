import unittest
from Lab5 import BFS_shortest_path 

class TestBFS(unittest.TestCase):
    def test_1(self):
        matrix = [
            [1, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1] 
        ]
        start = (0, 0)
        end = (3,1)
        rows, cols = 4, 4
        
        result = BFS_shortest_path(start, end, rows, cols, matrix)
        
        self.assertEqual(result, 4)
        
    def test_2(self):
        matrix = [
            [1, 1, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 0, 1] 
        ]
        start = (0, 0)
        end = (0, 2)
        rows, cols = 4, 4
        
        result = BFS_shortest_path(start, end, rows, cols, matrix)
         
        self.assertEqual(result, -1)
    
    def test_3(self):
        matrix = [
            [0, 1, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 0, 1] 
        ]
        start = (0, 1)
        end = (0, 0)
        rows, cols = 4, 4
        
        result = BFS_shortest_path(start, end, rows, cols, matrix)
         
        self.assertEqual(result, -1)
        
    def test_4(self):
        matrix = [
            [1, 1, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 0, 1] 
        ]
        start = (2, 1)
        end = (0, 0)
        rows, cols = 4, 4
        
        result = BFS_shortest_path(start, end, rows, cols, matrix)
         
        self.assertEqual(result, 3)
            
if __name__ == "__main__":
    unittest.main()
    