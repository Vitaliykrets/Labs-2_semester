import unittest

def find_three_sum(array, P):
        
        for num_1 in range(len(array)):
                value = list()
                for num_2 in range(num_1 + 1, len(array)):
                        num_3 = P - array[num_1] - array[num_2]
                        if num_3 in value and num_3 != array[num_1] and num_3 != array[num_2]:
                                return True
                        value.append(array[num_2])
                        
        return False

class Test_Robot_Find_Three_sum(unittest.TestCase):
    def test_case_1(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        P = 6
        self.assertTrue(find_three_sum(array, P))
        
    def test_case_2(self):
        array = [5, 3, 0, 3, 2, 1, 0, 4, -1, 23, 0]
        P = 0
        self.assertTrue(find_three_sum(array, P))
        
    def test_case_3(self):
        array = [0, 0, 1, 6, -23, 5, 2, 1, 2, 5, 23, 42, 31, 2]
        P = 100
        self.assertFalse(find_three_sum(array, P))
        
    def test_case_4(self):
        array = [-1, -2, -5, -3, -4, -7, -5, -7]
        P = -3
        self.assertFalse(find_three_sum(array, P))
        
if __name__ == "__main__":
    unittest.main()
 