import unittest
from Lab3.main import BinaryTree, find_successor


class TestFindInOrderTraversal(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(10)
        root.left = BinaryTree(5)
        root.right = BinaryTree(15)
        root.left.left = BinaryTree(3)
        root.left.right = BinaryTree(7)
        root.right.right = BinaryTree(20)
        root.right.left = BinaryTree(12)

        node = root.right
        successor = find_successor(root, node)
        self.assertEqual(successor, 20)


    def test_case_2(self):
        root = BinaryTree(50)
        root.left = BinaryTree(30)
        root.right = BinaryTree(70)
        root.left.left = BinaryTree(20)
        root.left.right = BinaryTree(40)
        root.right.right = BinaryTree(80)
        root.right.left = BinaryTree(60)

        node = root.right
        successor = find_successor(root, node)
        self.assertEqual(successor, 80)


    def test_case_3(self):
        root = BinaryTree(5)
        root.left = BinaryTree(3)
        root.right = BinaryTree(7)
        root.left.left = BinaryTree(2)
        root.left.right = BinaryTree(4)
        root.right.right = BinaryTree(8)
        root.right.left = BinaryTree(6)

        node = root.right
        successor = find_successor(root, node)
        self.assertEqual(successor, 8)


if __name__ == '__main__':
    unittest.main()
