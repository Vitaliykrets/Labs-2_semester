import unittest

def transform_for_robot(array):
    m = len(array)  
    n = len(array[0]) 
    result = []
    
    for x in range(m):
        for y in range(n):
            if x % 2 == 0:
                result.append(array[x][y])
            else:
                result.append(array[x][n - 1 - y])
    
    return result


class TestRobotGardener(unittest.TestCase):
    def test_m2_n4(self):
        input_array = [
            [1, 2, 3, 4],
            [8, 7, 6, 5]
        ]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        result = transform_for_robot(input_array)
        self.assertEqual(result, expected)
    
    def test_m5_n5(self):
        input_array = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        expected = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15, 20, 19, 18, 17, 16, 21, 22, 23, 24, 25]
        result = transform_for_robot(input_array)
        self.assertEqual(result, expected)
    
    def test_n1_m6(self):
        input_array = [
            [1],
            [-3],
            [7],
            [42],
            [0],
            [4]
        ]
        expected = [1, -3, 7, 42, 0, 4] 
        result = transform_for_robot(input_array)
        self.assertEqual(result, expected)
        

if __name__ == '__main__':
    unittest.main()