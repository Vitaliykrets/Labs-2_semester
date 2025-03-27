class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder_traversal(node, result=None):
    if result is None:
        result = []
    if node:
        inorder_traversal(node.left, result)
        result.append(node.data)
        inorder_traversal(node.right, result)
    return result


def find_successor(root, target): 
    successor = None
    min_distance = float('inf')

    for i, value in enumerate(inorder_list):
        if value > target:
            distance = abs(i - inorder_list.index(target))
            if distance < min_distance:
                min_distance = distance
                successor = value
                
    return successor


if __name__ == "__main__":
    root = BinaryTree(11)
    root.left = BinaryTree(10)
    root.right = BinaryTree(9)
    root.left.right = BinaryTree(7)
    root.right.left = BinaryTree(3)
    root.left.left = BinaryTree(5)
    root.right.right = BinaryTree(12)

    inorder_list = inorder_traversal(root)
    print(f"In-order traversal list: {inorder_list}")  
    
    target = int(input("Enter a node value to find it`s successor: "))
    
    successor = find_successor(root, target)
    
    if successor:
        print(f"Successor for a node {target} is a node with value {successor}")
    else:
        print(f"Successor for a node {target} not found")
