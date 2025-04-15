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

def BFS_shortest_path(start, end, rows, cols, matrix):
    if matrix[start[0]][start[1]] == 0 or matrix[end[0]][end[1]] == 0:
        return -1
    else:   
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        queue = [(start[0], start[1], 0)]
        visited[start[0]][start[1]] = True

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            x, y, dist = queue.pop(0)

            if (x, y) == end:
                return dist

            for dx, dy in directions:
                n_x, n_y = x + dx, y + dy

                if 0 <= n_x < rows and 0 <= n_y < cols and matrix[n_x][n_y] == 1 and not visited[n_x][n_y]:
                    visited[n_x][n_y] = True
                    queue.append((n_x, n_y, dist + 1))

        return -1



def output(file, result):
    with open(file, "w") as f:
        f.write(str(result))


def main():
    input_file = "Input.txt"
    output_file_path = "Output.txt"

    start, end, rows, cols, matrix = read_input(input_file)
    shortest_distance = BFS_shortest_path(start, end, rows, cols, matrix)
    output(output_file_path, shortest_distance)

if __name__ == "__main__":
    main()
