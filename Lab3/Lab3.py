class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


def find_successor(node):
    if node.right:
        current = node.right
        while current.left:
            current = current.left
        return current
    
    current = node
    while current.parent and current.parent.right == current:
        current = current.parent
        
    if current.parent:
        return current.parent
    return None


if __name__ == "__main__":
    root = BinaryTree(10)
    root.left = BinaryTree(5)
    root.right = BinaryTree(15)
    root.left.left = BinaryTree(3)
    root.left.right = BinaryTree(7)
    root.right.right = BinaryTree(20)
    root.right.left = BinaryTree(12)
    root.right.right.left = BinaryTree(19) 

    root.left.parent = root
    root.right.parent = root
    root.left.left.parent = root.left
    root.left.right.parent = root.left
    root.right.right.parent = root.right
    root.right.left.parent = root.right
    root.right.right.left.parent = root.right.right

    node = root.right
    successor = find_successor(node)
    if successor:
        print(f"Successor for a node {node.data} is a node with value {successor.data}")
    else:
        print(f"Successor for a node {node.data} not found")
