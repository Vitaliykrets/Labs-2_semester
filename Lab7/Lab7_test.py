import unittest
from Lab7 import search

class TestRabinKarp(unittest.TestCase):
    def test_case_1(self):
        haystack = "AABAACAADAABAABA"
        needle = "AABA"
        expected_result = [0, 9, 12]
        
        result = search(haystack, needle)
        
        self.assertEqual(result, expected_result)

    def test_case_2(self):
        haystack = "ABCDABCDABCF!"
        needle = "H"
        expected_result = []
        
        result = search(haystack, needle)
        
        self.assertEqual(result, expected_result)

    def test_case_3(self):
        haystack = "AABAACAADAABAABA"
        needle = ""
        expected_result = []
        
        result = search(haystack, needle)
        
        self.assertEqual(result, expected_result)

    def test_case_4(self):
        haystack = "sh"
        needle = "longerneedlelongerneedle"
        expected_result = []
        
        result = search(haystack, needle)
        
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
