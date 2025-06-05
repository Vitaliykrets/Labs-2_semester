def read_matrix(filename):
    try:
        with open(filename, 'r') as file:
            matrix = [list(map(int, line.strip().split(','))) for line in file if line.strip()]
        
        if not matrix or is_not_square(matrix):
            print("Error: Matrix is empty or not square")
            return None

        return matrix

    except FileNotFoundError:
        print(f"File {filename} not found")
        return None

    except Exception:
        print("Error: Invalid data format in file")
        return None


def is_not_square(matrix):
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return True
    return False


def prim_mst(matrix):
    n = len(matrix)
    visited = [False] * n
    min_edge = [float('inf')] * n
    min_edge[0] = 0
    parent = [-1] * n
    total_length = 0

    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or min_edge[i] < min_edge[u]):
                u = i

        if min_edge[u] == float('inf'):
            return None, None

        visited[u] = True
        total_length += min_edge[u]

        for v in range(n):
            if matrix[u][v] > 0 and not visited[v] and matrix[u][v] < min_edge[v]:
                min_edge[v] = matrix[u][v]
                parent[v] = u

    return total_length, parent


def build_mst_tree(parent):
    tree = {}
    for child, par in enumerate(parent):
        if par != -1:
            if par not in tree:
                tree[par] = []
            tree[par].append(child)
    return tree


def print_mst_tree_graph(parent, matrix):
    tree = build_mst_tree(parent)


    def visual_print(node, prefix=""):
        if node not in tree:
            return

        children = tree[node]
        for i, child in enumerate(children):
            connector = "|--- " if i == len(children)-1 else "|--- "
            print(prefix + connector + f"{child}  ({matrix[node][child]})")
            new_prefix = prefix + ("     " if i == len(children)-1 else "|   ")
            visual_print(child, new_prefix)

    print("Minimal Spanning Tree: ")
    print(f"{0}")
    visual_print(0)


def main():
    filename = 'islands.csv'
    matrix = read_matrix(filename)
    if matrix is None:
        return
    
    result, parent = prim_mst(matrix)
    if result is None:
        print("The graph is not connected! Can't connect all islands.")
    else:
        print_mst_tree_graph(parent, matrix)
        print(f"\nTotal weight of MST: {result}")


if __name__ == "__main__":
    main()
