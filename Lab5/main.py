def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()

    start = tuple(map(int, lines[0].strip().split(",")))
    end = tuple(map(int, lines[1].strip().split(",")))
    rows, cols = map(int, lines[2].strip().split(","))

    matrix = []
    for line in lines[3:]:
        row = list(map(int, line.strip().split()))
        matrix.append(row)

    return start, end, rows, cols, matrix


class Graph:
    def __init__(self, matrix, rows, cols):
        self.adj_list = {}
        self.rows = rows
        self.cols = cols
        self.build_graph(matrix)


    def in_bounds(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols


    def build_graph(self, matrix):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for x in range(self.rows):
            for y in range(self.cols):
                if matrix[x][y] == 1:
                    node = (x, y)
                    self.adj_list[node] = []
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if self.in_bounds(nx, ny) and matrix[nx][ny] == 1:
                            self.adj_list[node].append((nx, ny))


class BFS:
    def __init__(self, graph):
        self.graph = graph


    def shortest_path(self, start, end):
        if start not in self.graph.adj_list or end not in self.graph.adj_list:
            return -1

        visited = []
        queue = [(start, 0)]
        visited.append(start)
        i = 0

        while i < len(queue):
            current, dist = queue[i]
            i += 1

            if current == end:
                return dist

            for neighbor in self.graph.adj_list.get(current, []):
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append((neighbor, dist + 1))

        return -1


def output(file, result):
    with open(file, "w") as f:
        f.write(str(result))


def main():
    input_file = "Input.txt"
    output_file_path = "Output.txt"

    start, end, rows, cols, matrix = read_input(input_file)
    graph = Graph(matrix, rows, cols)
    bfs = BFS(graph)
    shortest_distance = bfs.shortest_path(start, end)
    output(output_file_path, shortest_distance)


def BFS_shortest_path(start, end, rows, cols, matrix):
    graph = Graph(matrix, rows, cols)
    bfs = BFS(graph)
    return bfs.shortest_path(start, end)


if __name__ == "__main__":
    main()
