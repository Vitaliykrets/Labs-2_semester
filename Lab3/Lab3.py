class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

def find_successor(node):
    if node.right:
        successor = node.right
        while successor.left:
            successor = successor.left
        return successor

    current = node
    while current.parent and current.parent.right == current:
        current = current.parent

    if current.parent:
        return current.parent
    return None


if __name__ == '__main__':
    root = BinaryTree(10)
    root.left = BinaryTree(5)
    root.right = BinaryTree(15)
    root.left.left = BinaryTree(3)
    root.left.right = BinaryTree(7)
    root.right.right = BinaryTree(20)
    root.right.left = BinaryTree(12)

    root.left.parent = root
    root.right.parent = root.right
    root.left.left.parent = root.left
    root.left.right.parent = root.left
    root.right.right.parent = None
    root.right.left.parent = root.right

    node = root.right.right
    successor = find_successor(node)
    if successor:
        print(f"Successor for a node {node.data} — a node with a value {successor.data}")
    else:
        print(f"Successor for a node {node.data} not found")
