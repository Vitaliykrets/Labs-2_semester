class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_nodes(self, nodes):
        if not nodes:
            return
        node_dict = {}
        for line in nodes:
            values = line.split()
            if values[0] not in node_dict:
                node_dict[values[0]] = TreeNode(int(values[0]))
            node = node_dict[values[0]]
            if not self.root:
                self.root = node
            if values[1] != "None":
                if values[1] not in node_dict:
                    node_dict[values[1]] = TreeNode(int(values[1]))
                node.left = node_dict[values[1]]
            if values[2] != "None":
                if values[2] not in node_dict:
                    node_dict[values[2]] = TreeNode(int(values[2]))
                node.right = node_dict[values[2]]

    def inorder_traversal(self, node):
        result = []
        stack = []
        current = node

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(current.value)
            current = current.right
        
        return result
    # def inorder_traversal(self, node, result=None):
    #     if result is None:
    #         result = []
    #     if node:
    #         self.inorder_traversal(node.left, result)
    #         result.append(node.value)
    #         self.inorder_traversal(node.right, result)
    #     return result

    def find_successor(self, inorder_values, target):
        successor = None
        min_distance = float('inf')

        for i, value in enumerate(inorder_values):
            if value > target:
                distance = abs(i - inorder_values.index(target))  
                if distance < min_distance:
                    min_distance = distance
                    successor = value
        return successor

    
    def print_tree(self, node, indent="", last='updown'):
        if node != None:
            if last == 'updown':  
                print(f"{indent}Root: {node.value}")
                indent += "    "
            elif last == 'left':  
                print(f"{indent}L--- {node.value}")
                indent += "|   "
            elif last == 'right':  
                print(f"{indent}R--- {node.value}")
                indent += "    "
            
            if node.left is None and node.right is None:  
                print(f"{indent}L--- None")
                print(f"{indent}R--- None")
            else:
                if node.left:
                    self.print_tree(node.left, indent, 'left')
                else:
                    print(f"{indent}L--- None")
                
                if node.right:
                    self.print_tree(node.right, indent, 'right')
                else:
                    print(f"{indent}R--- None")


def read_tree_from_file(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    tree = BinaryTree()
    tree.insert_nodes(lines)
    return tree


filename = "tree.txt" 
tree = read_tree_from_file(filename)
inorder_values = tree.inorder_traversal(tree.root)

tree.print_tree(tree.root)

print(f"In_order travelsal: {inorder_values}")

for value in inorder_values:
    successor = tree.find_successor(inorder_values, value)
    print(f"Successor to {value}: {successor if successor else 'None'}")
