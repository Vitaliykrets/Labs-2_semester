import unittest

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None  


def inorder_traversal(node, result=None):
    if result is None:
        result = []
    if node:
        inorder_traversal(node.left, result)
        result.append(node.data)
        inorder_traversal(node.right, result)
    return result


def find_successor(node): 
    inorder_list = inorder_traversal(node)
    
    successor = None
    for i in range(len(inorder_list) - 1):
        if inorder_list[i] == node.data:
            successor = inorder_list[i + 1] 
            break
    
    return successor


class TestFindInOrderTraversal(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(10)
        root.left = BinaryTree(5)
        root.right = BinaryTree(15)
        root.left.left = BinaryTree(3)
        root.left.right = BinaryTree(7)
        root.right.right = BinaryTree(20)
        root.right.left = BinaryTree(12)

        root.left.parent = root
        root.right.parent = root
        root.left.left.parent = root.left
        root.left.right.parent = root.left
        root.right.right.parent = root.right
        root.right.left.parent = root.right

        node = root.right
        successor = find_successor(node)
        self.assertEqual(successor, 20)

    def test_case_2(self):
        root = BinaryTree(50)
        root.left = BinaryTree(30)
        root.right = BinaryTree(70)
        root.left.left = BinaryTree(20)
        root.left.right = BinaryTree(40)
        root.right.right = BinaryTree(80)
        root.right.left = BinaryTree(60)

        root.left.parent = root
        root.right.parent = root
        root.left.left.parent = root.left
        root.left.right.parent = root.left
        root.right.right.parent = root.right
        root.right.left.parent = root.right

        node = root.right
        successor = find_successor(node)
        self.assertEqual(successor, 80)

    def test_case_3(self):
        root = BinaryTree(5)
        root.left = BinaryTree(3)
        root.right = BinaryTree(7)
        root.left.left = BinaryTree(2)
        root.left.right = BinaryTree(4)
        root.right.right = BinaryTree(8)
        root.right.left = BinaryTree(6)

        root.left.parent = root
        root.right.parent = root
        root.left.left.parent = root.left
        root.left.right.parent = root.left
        root.right.right.parent = root.right
        root.right.left.parent = root.right

        node = root.right
        successor = find_successor(node)
        self.assertEqual(successor, 8)

if __name__ == '__main__':
    unittest.main()
